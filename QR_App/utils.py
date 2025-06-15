import qrcode
import base64
from io import BytesIO

def MakeQR(url, fill_color="#000000", back_color="#ffffff"):
    if not url:
        return None
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    qr_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return qr_str








   


