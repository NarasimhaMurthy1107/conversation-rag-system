def build_persona(messages):
    habits = set()
    personality = set()
    style = set()

    for msg in messages:
        m = msg.lower()

        if "sleep" in m or "late night" in m:
            habits.add("late sleeper")

        if "study" in m or "college" in m:
            habits.add("student")

        if "cook" in m or "food" in m:
            habits.add("likes cooking")

        if "haha" in m or "lol" in m:
            personality.add("humorous")

        if "love" in m or "enjoy" in m:
            personality.add("positive")

        if len(m.split()) < 5:
            style.add("short messages")

        if "!" in m:
            style.add("expressive")

    return {
        "habits": list(habits),
        "personality": list(personality),
        "communication_style": list(style)
    }