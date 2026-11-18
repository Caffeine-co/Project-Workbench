"""命令行程序：无需 NoneBot/LLM 即可跑通 World → Life。"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_scenario
from .store import SQLiteStore


def main() -> None:
    parser = argparse.ArgumentParser(description="World-Life 无 LLM 模拟器")
    parser.add_argument("scenario", type=Path, help="场景配置 JSON 路径")
    parser.add_argument("--hours", type=int, default=72, help="从当前存档再推进多少小时")
    parser.add_argument("--db", type=Path, default=Path("data/worldlife.db"))
    parser.add_argument("--tail", type=int, default=12, help="输出最近多少条事件")
    args = parser.parse_args()
    if args.hours < 0 or args.tail < 0:
        parser.error("--hours 与 --tail 不能为负数")

    scenario = load_scenario(args.scenario) # 读取并检查配置，把几个 JSON 组成完整场景
    with SQLiteStore(args.db) as store: # 打开数据库，准备恢复或建立模拟
        runtime = store.load_or_create(scenario)    # 有存档则恢复，没有则创建全新的 WorldRuntime
        before = runtime.minute
        runtime.run_until(before + args.hours * 60) # 真正推进世界时间并执行其中的行为，
        store.save(runtime) # 保存世界当前状态和本次新增的事件日志
        print(f"World: {scenario.world.id} | {before} -> {runtime.minute} minutes")
        print("Resources:", json.dumps(runtime.resources, ensure_ascii=False))
        for actor in runtime.lives.values():
            print(f"Life: {actor.id} @ {actor.location}")
            print("Drives:", json.dumps({k: round(v, 2) for k, v in actor.drives.items()}, ensure_ascii=False))
            print("Busy:", actor.busy)
        print(f"Last {args.tail} events:")
        for minute, kind, aid, details in store.recent_events(args.tail):
            print(f"  t={minute:>5} | {kind:<22} | {aid or '-':<12} | {details}")


if __name__ == "__main__":
    main()