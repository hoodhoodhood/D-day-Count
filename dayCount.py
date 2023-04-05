import datetime
import tkinter as tk
from PIL import Image, ImageTk


D_DAY = datetime.datetime(2023, 4, 23)


class CountdownWidget:
    def __init__(self, master):
        # 위젯 폰트 및 크기 설정
        self.font_size = int(master.winfo_screenheight() / 10)
        self.font = ("Helvetica", self.font_size)

        # 위젯 프레임
        self.widget_frame = tk.Frame(master, bg="black")

        # 남은 시간 출력 라벨
        self.remaining_time_var = tk.StringVar()
        self.remaining_time_label = tk.Label(
            self.widget_frame, textvariable=self.remaining_time_var, font=self.font, fg="white", bg="black")
        self.remaining_time_label.pack(pady=self.font_size * 2)

        # 프레임 배치
        self.widget_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.update()

    def update(self):
        # 현재 시간 계산
        now = datetime.datetime.now()

        # D-day까지 남은 시간 계산
        remaining_time = D_DAY - now

        # D-day가 지난 경우
        if remaining_time.days < 0:
            self.remaining_time_var.set("D-day가 지났습니다.")
            return

        # 남은 시간 출력
        self.remaining_time_var.set("정보처리기사실기\nD-{:d} {:02d}:{:02d}:{:02d}".format(
            remaining_time.days,
            remaining_time.seconds // 3600,
            (remaining_time.seconds % 3600) // 60,
            remaining_time.seconds % 60
        ))

        # 1초 대기 후 다시 업데이트
        self.remaining_time_label.after(1000, self.update)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("D-day Countdown")
    root.attributes("-fullscreen", True)

    # 이미지 파일 열기
    image = Image.open("bg3.jpg")
    # 이미지 크기 조정
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    # PhotoImage 객체 생성
    photo = ImageTk.PhotoImage(image)

    # Canvas 위젯 생성
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()
    # 이미지를 Canvas에 삽입
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    countdown_widget = CountdownWidget(canvas)

    root.mainloop()