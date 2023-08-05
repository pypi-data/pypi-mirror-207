from typing import Any


NAME = "fake"
FAKE_TEST_DATA = [
    # T = 0
    [
        {
            "id": 1,
            "url": "https://example.com/1",
            "name": "test-1",
            "display_name": "Test User 1",
            "avatar": "https://example.com/avatar-1.jpg",
            "description": "I am Test User 1.",
        },
        {
            "id": 2,
            "url": "https://example.com/2",
            "name": "test-2",
            "display_name": "Test User 2",
            "avatar": "https://example.com/avatar-2.jpg",
            "description": "I am Test User 2.",
        },
        {
            "id": 3,
            "url": "https://example.com/3",
            "name": "test-3",
            "display_name": "Test User 3",
            "avatar": "https://example.com/avatar-3.jpg",
            "description": "I am Test User 3.",
        },
    ],

    # T = 1
    [
        {
            "id": 1,
            "url": "https://example.com/1",
            "name": "test-1",
            "display_name": "Test User 1",
            "avatar": "https://example.com/avatar-1.jpg",
            "description": "I am Test User 1.",
        },
        {
            "id": 2,
            "url": "https://example.com/2",
            "name": "test-2",
            "display_name": "Test User 2",
            "avatar": "https://example.com/avatar-2.jpg",
            "description": "I am Test User 2.",
        },
        {
            "id": 3,
            "url": "https://example.com/3",
            "name": "test-3",
            "display_name": "Test User 3",
            "avatar": "https://example.com/avatar-3.jpg",
            "description": "I am Test User 3.",
        },
    ],

    # T = 2
    [
        {
            "id": 1,
            "url": "https://example.com/1",
            "name": "test-1",
            "display_name": "Test User 1",
            "avatar": "https://example.com/avatar-1.jpg",
            "description": "I am Test User 1.",
        },
        {
            "id": 5,
            "url": "https://example.com/5",
            "name": "test-5",
            "display_name": "Test User 5",
            "avatar": "https://example.com/avatar-5.jpg",
            "description": "I am Test User 5.",
        },
    ],

    # T = 3
    [
        {
            "id": 1,
            "url": "https://example.com/1",
            "name": "test-1",
            "display_name": "Test User 1",
            "avatar": "https://example.com/avatar-1.jpg",
            "description": "I am Test User 1.",
        },
        {
            "id": 5,
            "url": "https://example.com/5",
            "name": "test-5-namechanged",
            "display_name": "Test User 5 Name Changed",
            "avatar": "https://example.com/avatar-5.jpg",
            "description": "I am Test User 5, I changed name.",
        },
    ],
]

def fetch(config: dict[str, Any]) -> dict:
    index = int(config['time'])
    return FAKE_TEST_DATA[index]
