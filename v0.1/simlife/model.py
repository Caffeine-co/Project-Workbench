"""数据模型：规范的事实来源与可变运行状态分离。"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class DriveSpec:    # 个体驱动设定，决定变化规则
    """需求的缺口值：0 表示已满足，100 表示非常迫切。不是医学测量。当前demo统一使用需求缺口语义"""
    initial: float  # 初始值
    rise_per_hour: float
    threshold: float    # 临界点，开始通过该需求产生行动收益
    priority: float # 重视权重


@dataclass(frozen=True)
class Persona:  # 角色个体模具
    id: str
    drives: dict[str, DriveSpec]
    move_multiplier: float = 1.0


@dataclass(frozen=True)
class Facility:
    id: str
    location: str
    duration: int  # 分钟
    effects: dict[str, float]  # 对需求缺口的变化，例如 -40 表示缓解
    resource: str | None = None
    units: float = 0.0


@dataclass(frozen=True)
class WorldDefinition:
    id: str
    connections: dict[str, dict[str, int]]
    facilities: dict[str, Facility]
    initial_resources: dict[str, tuple[float, float]]  # 当前库存、容量
    external_events: list[dict[str, Any]]


@dataclass
class LifeState:    # 描述当前运行状态，是该个体在世界中实际演化出的结果
    id: str
    persona_id: str
    location: str
    known_locations: list[str]
    drives: dict[str, float]
    # 每个需求最后一次被离散事件改变时的锚点；保证任意切分时间推进后结果一致。
    anchors: dict[str, dict[str, float | int]] = field(default_factory=dict)
    """
    锚点
    例如：
    "anchors": {
        "thirst": {
            "minute": 129,
            "value": 0.0
        }
    }
    意思是：
        在第 129 分钟，口渴缺口经过某次离散事件结算后，确定为 0。之后的自然变化应从这个时间点和数值重新计算。
    这样程序不需要每推进一分钟就修改一次口渴状态，也不需要反复累加小数值。
    """
    busy: dict[str, Any] | None = None
    """
    为什么有 busy？
    例如：
    life.busy = {
        "kind": "move",
        "to": "hall",
        "finish": 122
    }
    这表示角色正在移动，还没有完成。
    在第 120 分钟开始行动，不意味着第 120 分钟就已经到达目的地。
    只有对应的 move_finished 事件在第 122 分钟被执行后，World 才会修改 life.location。
    """

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id, "persona_id": self.persona_id,
            "location": self.location, "known_locations": self.known_locations,
            "drives": self.drives, "anchors": self.anchors, "busy": self.busy,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> LifeState:
        return cls(**data)


@dataclass
class Scenario: # 场景装配
    world: WorldDefinition
    personas: dict[str, Persona]  # actor_id -> Persona
    initial_lives: dict[str, LifeState]
    fingerprint: str


@dataclass(order=True)
class QueuedEvent:
    """事件只按 time/sequence 排序，其余元数据不是排序字段。"""
    minute: int
    priority: int
    sequence: int
    kind: str = field(compare=False)
    payload: dict[str, Any] = field(default_factory=dict, compare=False)

    def to_dict(self) -> dict[str, Any]:
        return {"minute": self.minute, "priority": self.priority,
                "sequence": self.sequence, "kind": self.kind, "payload": self.payload}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> QueuedEvent:
        return cls(**data)
