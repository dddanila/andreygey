from telebot import types


# Main menu
main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='🛍 Приобрести', callback_data='catalog'),
    types.InlineKeyboardButton(text='👤 Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='ℹ️ Информация', callback_data='info'),
    types.InlineKeyboardButton(text='🛒 Мои приватки', callback_data='purchases'),
    types.InlineKeyboardButton(text='💸 Пополнить баланс', callback_data='pay_enter'),
)
main_menu.add(
    #types.InlineKeyboardButton(text='👥 Реферальная сеть', callback_data='referral_web'),
)

pay_enter = types.InlineKeyboardMarkup(row_width=2)
pay_enter.add(
    types.InlineKeyboardButton(text='💳 Qiwi', callback_data='replenish_balance'),
    types.InlineKeyboardButton(text='💳 Банковская карта', callback_data='replenish_balance'),
    #types.InlineKeyboardButton(text='💎 Криптовалюта(Временно не работает!)', callback_data='crypto_pay'),   
)
pay_enter.add(
    types.InlineKeyboardButton(
        text="⬅️ Назад",
        callback_data='exit_to_menu')
)

crypto_pay = types.InlineKeyboardMarkup()
crypto_pay.add(
    types.InlineKeyboardButton(text="⬅️ Назад", callback_data='exit_to_menu')
)

# Admin menu
admin_menu = types.InlineKeyboardMarkup(row_width=2)
admin_menu.add(types.InlineKeyboardButton(text='Управление каталогом', callback_data='catalog_control'))
admin_menu.add(types.InlineKeyboardButton(text='Управление товаром', callback_data='section_control'))
admin_menu.add(types.InlineKeyboardButton(text='Изменить баланс', callback_data='give_balance'))
admin_menu.add(types.InlineKeyboardButton(text='Рассылка', callback_data='admin_sending_messages'))
admin_menu.add(types.InlineKeyboardButton(text='Топ рефералов(доходы)', callback_data='admin_top_ref'))
admin_menu.add(
    types.InlineKeyboardButton(text='Информаци', callback_data='admin_info'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_admin_menu')
)

# Admin control
admin_menu_control_catalog = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_catalog.add(
    types.InlineKeyboardButton(text='Добавить раздел в каталог', callback_data='add_section_to_catalog'),
    types.InlineKeyboardButton(text='Удалить раздел в каталог', callback_data='del_section_to_catalog'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Admin control section
admin_menu_control_section = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_section.add(
    types.InlineKeyboardButton(text='Добавить товар в раздел', callback_data='add_product_to_section'),
    types.InlineKeyboardButton(text='Удалить товар из раздела', callback_data='del_product_to_section'),
    types.InlineKeyboardButton(text='Загрузить товар', callback_data='download_product'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Back to admin menu
back_to_admin_menu = types.InlineKeyboardMarkup(row_width=1)
back_to_admin_menu.add(
    types.InlineKeyboardButton(text='Вернуться в админ меню', callback_data='back_to_admin_menu')
)

btn_purchase = types.InlineKeyboardMarkup(row_width=2)
btn_purchase.add(
    types.InlineKeyboardButton(text='Купить', callback_data='buy'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_to_menu')
)

btn_ok = types.InlineKeyboardMarkup(row_width=3)
btn_ok.add(
    types.InlineKeyboardButton(text='Понял', callback_data='btn_ok')
)
to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='to_close')
)




