from django.shortcuts import render
import django.http as http

tips = {
  "underweight": {
    "name": "Kekurangan Berat Badan",
    "bmi_range": "Dibawah 18.5",
    "tips": [
      {
        "tip": "Konsultasikan dengan ahli gizi untuk rencana peningkatan berat badan yang sehat.",
        "type": "nutrition"
      },
      {
        "tip": "Tambahkan kalori sehat dalam diet Anda, seperti kacang-kacangan, biji-bijian, dan produk susu.",
        "type": "nutrition"
      },
      {
        "tip": "Tingkatkan asupan protein untuk membantu membangun otot.",
        "type": "nutrition"
      },
      {
        "tip": "Jangan melewatkan waktu makan dan pertimbangkan untuk makan lebih sering dengan porsi kecil.",
        "type": "nutrition"
      },
      {
        "tip": "Lakukan latihan kekuatan untuk meningkatkan massa otot.",
        "type": "exercise"
      }
    ]
  },
  "normal_weight": {
    "name": "Berat yang ideal",
    "bmi_range": "18.5 - 24.9",
    "tips": [
      {
        "tip": "Pertahankan pola makan seimbang yang kaya akan buah-buahan, sayuran, protein tanpa lemak, dan biji-bijian.",
        "type": "nutrition"
      },
      {
        "tip": "Lakukan aktivitas fisik secara teratur, seperti jalan kaki, berlari, atau bersepeda.",
        "type": "exercise"
      },
      {
        "tip": "Jaga hidrasi dengan minum cukup air setiap hari.",
        "type": "hydration"
      },
      {
        "tip": "Cukup tidur setiap malam untuk mendukung kesehatan secara keseluruhan.",
        "type": "lifestyle"
      },
      {
        "tip": "Hindari makanan olahan dan berlemak tinggi yang dapat mempengaruhi berat badan Anda.",
        "type": "nutrition"
      }
    ]
  },
  "overweight": {
    "name": "Kelebihan Berat Badan",
    "bmi_range": "25 - 29.9",
    "tips": [
      {
        "tip": "Kurangi asupan kalori dengan memilih makanan rendah lemak dan rendah gula.",
        "type": "nutrition"
      },
      {
        "tip": "Tingkatkan aktivitas fisik dengan berolahraga setidaknya 30 menit sehari.",
        "type": "exercise"
      },
      {
        "tip": "Perbanyak konsumsi sayuran, buah-buahan, dan biji-bijian dalam diet Anda.",
        "type": "nutrition"
      },
      {
        "tip": "Hindari minuman berkalori tinggi seperti soda dan jus manis.",
        "type": "nutrition"
      },
      {
        "tip": "Pertimbangkan untuk mengikuti program penurunan berat badan yang diawasi oleh profesional.",
        "type": "professional_advice"
      }
    ]
  },
  "obesity": {
    "name": "Obesitas",
    "bmi_range": "Lebih dari 30",
    "tips": [
      {
        "tip": "Konsultasikan dengan dokter atau ahli gizi untuk rencana penurunan berat badan yang aman.",
        "type": "professional_advice"
      },
      {
        "tip": "Lakukan perubahan gaya hidup dengan mengurangi makanan berkalori tinggi dan meningkatkan aktivitas fisik.",
        "type": "lifestyle"
      },
      {
        "tip": "Ikuti program latihan yang berfokus pada pembakaran lemak dan peningkatan kebugaran kardiovaskular.",
        "type": "exercise"
      },
      {
        "tip": "Buatlah catatan makanan untuk memantau asupan kalori harian Anda.",
        "type": "nutrition"
      },
      {
        "tip": "Pertimbangkan terapi perilaku untuk membantu mengubah kebiasaan makan dan aktivitas fisik.",
        "type": "professional_advice"
      }
    ]
  }
}


# Create your views here.
def main(request):
    return http.HttpResponse('Hello World this is new views from web')

def web_render(request):
    return render(request, 'main.html')

def orders_view(request):
    return render(request, 'orders.html')

def calculator_view(request):
    result = 0
    tipe = ""
    bmi_tips = {}
    bg = ""
    if request.method == 'POST':
        tinggi = int(request.POST['tinggi']) / 100
        berat = int(request.POST['berat'])

        result = round(berat / tinggi ** 2, 2)
        
        if result < 18.5:
            bg = 'bg-primary text-white'
            tipe = 'underweight'
            bmi_tips = tips[tipe]
        elif 18.5 <= result < 25:
            bg = 'bg-success text-white'
            tipe = 'normal_weight'
            bmi_tips = tips[tipe]
        elif 25 <= result < 30:
            bg = 'bg-warning text-black'
            tipe = "overweight"
            bmi_tips = tips[tipe]
        else:
            bg = 'bg-danger text-white'
            tipe = "obesity"
            bmi_tips = tips[tipe]
        
        
    return render(request, 'calculator.html', { 'result': result, 'tips': bmi_tips, 'tipe': tipe, 'bg': bg })

