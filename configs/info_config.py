def user_info_text(user):
    text = "👤 **Информация**"
    text += f"\n📌 **ID:** `{user.id}`"
    text += f"\n📝 **Имя:** `{user.first_name}`"
    text += f"\n🔐 **Ограничения:** `{user.is_restricted}`"
    text += f"\n💰 **Мошенник:** `{user.is_scam}`"
    text += f"\n⭐️ **Премиум:** `{user.is_premium}`"
    text += f"\n📎 **Ссылка:** `{user.mention}`"
    return text


def chat_info_text(chat):
    text = "👥 **Информация**"
    text += f"\n📌 **ID:** `{chat.id}`"
    text += f"\n📝 **Название:** `{chat.title}`"
    text += f"\n🔐 **Ограничения:** `{chat.is_restricted}`"
    text += f"\n💰 **Мошенники:** `{chat.is_scam}`"
    text += f"\n✅ **Верификация:** `{chat.is_verified}`"
    return text

