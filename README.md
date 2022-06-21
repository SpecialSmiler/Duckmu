# Bilibili API 第三方文档

- https://qinshixixing.gitbooks.io/bilibiliapi/content/

- [示例：获取直播间弹幕和礼物](https://bili.moyu.moe/#/examples/live?id=示例：获取直播间弹幕和礼物)

- https://pypi.org/project/bilibili-api/

# json

```json
{
    "room_display_id": 147107,
    "room_real_id": 147107,
    "type": "DANMU_MSG",
    "data": {
        "cmd": "DANMU_MSG",
        "info": [
            [
                0,
                1,
                25,
                16777215,
                1655223770873,
                1655223663,
                0,
                "d3cfc1fe",
                0,
                0,
                0,
                "",
                0,
                "{}",
                "{}",
                {
                    "mode": 0,
                    "show_player_type": 0,
                    "extra": "{\"send_from_me\":false,\"mode\":0,\"color\":16777215,\"dm_type\":0,\"font_size\":25,\"player_mode\":1,\"show_player_type\":0,\"content\":\"测试2\",\"user_hash\":\"3553608190\",\"emoticon_unique\":\"\",\"bulge_display\":0,\"recommend_score\":10,\"main_state_dm_color\":\"\",\"objective_state_dm_color\":\"\",\"direction\":0,\"pk_direction\":0,\"quartet_direction\":0,\"yeah_space_type\":\"\",\"yeah_space_url\":\"\",\"jump_to_url\":\"\",\"space_type\":\"\",\"space_url\":\"\"}"
                }
            ],
            "测试2",
            [
                2209180,
                "特笑师",
                0,
                0,
                0,
                10000,
                1,
                ""
            ],
            [],
            [
                14,
                0,
                6406234,
                ">50000",
                1
            ],
            [
                "",
                ""
            ],
            0,
            0,
            null,
            {
                "ts": 1655223770,
                "ct": "6C3A7F90"
            },
            0,
            0,
            null,
            null,
            0,
            210
        ]
    }
}
```

```json
{'room_display_id': 147107, 'room_real_id': 147107, 'type': 'DANMU_MSG', 'data': {'cmd': 'DANMU_MSG', 'info': [[0, 1, 25, 16777215, 1655224372067, 1655223663, 0, 'd3cfc1fe', 0, 0, 0, '', 0, '{}', '{}', {'mode': 0, 'show_player_type': 0, 'extra': '{"send_from_me":false,"mode":0,"color":16777215,"dm_type":0,"font_size":25,"player_mode":1,"show_player_type":0,"content":"测试3","user_hash":"3553608190","emoticon_unique":"","bulge_display":0,"recommend_score":10,"main_state_dm_color":"","objective_state_dm_color":"","direction":0,"pk_direction":0,"quartet_direction":0,"yeah_space_type":"","yeah_space_url":"","jump_to_url":"","space_type":"","space_url":""}'}], '测试3', [2209180, '特笑师', 0, 0, 0, 10000, 1, ''], [], [14, 0, 6406234, '>50000', 1], ['', ''], 0, 0, None, {'ts': 1655224372, 'ct': 'A51A15D5'}, 0, 0, None, None, 0, 210]}}
```

