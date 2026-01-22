def mailContext(name, phone, email, line_id, service_list, msg):
    msg = 'Dear All\n\n客戶諮詢單特此通知。\n' + \
        f'客戶名稱: {name}\n' + \
        f'聯絡電話: {phone}\n' + \
        f'email: {email}\n' + \
        f'Line ID: {line_id}\n' + \
        f'主要諮詢項目: {service_list}\n' + \
        f'備註: {msg}\n\n' + \
        '以上。'
    return msg