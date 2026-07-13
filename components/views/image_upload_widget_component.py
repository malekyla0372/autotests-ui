from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.file_input import FileInput
from elements.button import Button
from elements.text import Text
from elements.icon import Icon


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview image')

        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon',
                                           'Image upload info icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text',
                                            'Image upload info title')
        self.image_upload_info_description = Text(page, f'{identifier}-image-upload-widget-info-description-text',
                                                  'Image upload info description')

        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload image button')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove image button')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload image')

    def check_visible(self, index: int, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible(index=index)

        self.image_upload_info_title.check_visible(index=index)
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file', index=index)

        self.image_upload_info_description.check_visible(index=index)
        self.image_upload_info_description.check_have_text('Recommended file size 540X300', index=index)

        self.upload_button.check_visible(index=index)

        if is_image_uploaded:
            self.remove_button.check_visible(index=index)
            self.preview_image.check_visible(index=index)

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here',
                index=index
            )

    def click_remove_image_button(self, index: int):
        self.remove_button.click(index=index)

    def upload_preview_image(self, file: str, index: int):
        self.upload_input.set_input_files(file, index=index)
