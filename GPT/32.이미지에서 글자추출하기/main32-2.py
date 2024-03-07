from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
from PIL import Image as PILImage
import pytesseract

class ImageToTextConverter(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageToTextConverter, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.image_label = Image()
        self.add_widget(self.image_label)

        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)

        self.select_button = Button(text="이미지 선택")
        self.select_button.bind(on_press=self.selectImage)
        self.add_widget(self.select_button)

        self.convert_button = Button(text="변환", disabled=True)
        self.convert_button.bind(on_press=self.convertText)
        self.add_widget(self.convert_button)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def selectImage(self, instance):
        file_path = self.file_chooser.selection and self.file_chooser.selection[0] or None
        if file_path:
            self.image_label.source = file_path
            self.image_label.reload()
            self.convert_button.disabled = False
            self.file_path = file_path

    def convertText(self, instance):
        text = pytesseract.image_to_string(PILImage.open(self.file_path))
        self.result_label.text = text

class ImageToTextApp(App):
    def build(self):
        return ImageToTextConverter()

if __name__ == "__main__":
    ImageToTextApp().run()
