_ = {
    "cognition_usage": {},
    "enabled": {
        "bed": True,
        "meal": True,
        "practice_drawing": False,
        "practice_reading": True,
        "tap": True
    },
    "lives": {
        "resident_01": {
            "action_ticket": 6,
            "anchors": {
                "creative_urge": {
                    "minute": 0,
                    "value": 12
                },
                "fatigue": {
                    "minute": 0,
                    "value": 15
                },
                "hunger": {
                    "minute": 0,
                    "value": 20
                },
                "sleep_pressure": {
                    "minute": 0,
                    "value": 25
                },
                "thirst": {
                    "minute": 249,
                    "value": 0
                }
            },
            "beliefs": {
                "bed": {
                    "duration": 240,
                    "effects": {
                        "fatigue": -55.0,
                        "sleep_pressure": -68.0
                    },
                    "last_result": None,
                    "last_seen": 240,
                    "last_used": None,
                    "location": "bedroom",
                    "tags": []
                },
                "meal": {
                    "duration": 25,
                    "effects": {
                        "hunger": -66.0
                    },
                    "last_result": None,
                    "last_seen": 249,
                    "last_used": None,
                    "location": "kitchen",
                    "tags": []
                },
                "practice_drawing": {
                    "duration": 90,
                    "effects": {
                        "creative_urge": -38.0,
                        "fatigue": 5.0
                    },
                    "last_result": "facility_disabled",
                    "last_seen": 254,
                    "last_used": 344,
                    "location": "studio",
                    "tags": [
                        "practice",
                        "skill:drawing"
                    ]
                },
                "practice_reading": {
                    "duration": 60,
                    "effects": {
                        "fatigue": 2.0
                    },
                    "last_result": None,
                    "last_seen": 344,
                    "last_used": None,
                    "location": "studio",
                    "tags": [
                        "practice",
                        "skill:reading"
                    ]
                },
                "tap": {
                    "duration": 4,
                    "effects": {
                        "thirst": -62.0
                    },
                    "last_result": "ok",
                    "last_seen": 249,
                    "last_used": 249,
                    "location": "kitchen",
                    "tags": []
                }
            },
            "blocked_reason": None,
            "busy": None,
            "commitments": [
                {
                    "kind": "practice",
                    "minute": 720,
                    "target": "practice_drawing"
                }
            ],
            "completed_goals": 0,
            "decision_ticket": 16,
            "drives": {
                "creative_urge": 16.8,
                "fatigue": 21.6,
                "hunger": 35.0,
                "sleep_pressure": 38.8,
                "thirst": 7.03
            },
            "emotion": {
                "arousal": 0.11771663,
                "valence": -0.05923659
            },
            "facts": {},
            "failed_until": {
                "practice_drawing": 524
            },
            "failure_counts": {
                "practice_drawing": 1
            },
            "goal": None,
            "goal_since": 344,
            "id": "resident_01",
            "known_edges": {
                "bedroom": {
                    "hall": 2
                },
                "hall": {
                    "bedroom": 2,
                    "kitchen": 3,
                    "studio": 2
                },
                "kitchen": {
                    "hall": 3
                },
                "studio": {
                    "hall": 2
                }
            },
            "known_locations": [
                "bedroom",
                "hall",
                "kitchen",
                "studio"
            ],
            "last_creative": -1440,
            "last_social": -1440,
            "location": "studio",
            "long_goals": {
                "drawing": {
                    "completed_at": None,
                    "created_at": 0,
                    "id": "drawing",
                    "progress": 4.0,
                    "status": "active",
                    "target": 40.0
                }
            },
            "memories": [
                {
                    "actors": [],
                    "kind": "failure",
                    "minute": 344,
                    "salience": 0.7,
                    "source": "world_event",
                    "text": "使用 practice_drawing 失败：facility_disabled"
                }
            ],
            "persona_id": "human_artist",
            "projects": {
                "art_portfolio": {
                    "completed_at": None,
                    "deadline": 10080,
                    "evidence": [],
                    "failures": 1,
                    "id": "art_portfolio",
                    "index": 0,
                    "priority": 0.9,
                    "retry_at": 464,
                    "start_minute": 0,
                    "status": "active",
                    "steps": [
                        {
                            "kind": "practice",
                            "target": "practice_drawing"
                        },
                        {
                            "kind": "practice",
                            "target": "practice_drawing"
                        },
                        {
                            "kind": "practice",
                            "target": "practice_drawing"
                        },
                        {
                            "kind": "practice",
                            "target": "practice_drawing"
                        }
                    ]
                }
            },
            "propositions": {},
            "relationships": {},
            "skills": {
                "drawing": 4.0
            },
            "visited": [
                "bedroom",
                "hall",
                "kitchen",
                "studio"
            ],
            "vitality": 95.6766667
        }
    },
    "minute": 360,
    "queue": [
        {
            "kind": "decide",
            "minute": 374,
            "payload": {
                "actor": "resident_01",
                "ticket": 16
            },
            "priority": 2,
            "sequence": 26
        },
        {
            "kind": "facility_enable",
            "minute": 900,
            "payload": {
                "facility": "practice_drawing"
            },
            "priority": 0,
            "sequence": 4
        },
        {
            "kind": "resource_add",
            "minute": 1440,
            "payload": {
                "amount": 12,
                "repeat_every_minutes": 1440,
                "resource": "water"
            },
            "priority": 0,
            "sequence": 1
        },
        {
            "kind": "resource_add",
            "minute": 1440,
            "payload": {
                "amount": 8,
                "repeat_every_minutes": 1440,
                "resource": "food"
            },
            "priority": 0,
            "sequence": 2
        }
    ],
    "resources": {
        "food": 10.0,
        "water": 17.0
    },
    "sequence": 26
}