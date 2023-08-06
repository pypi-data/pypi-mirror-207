class ExtensionsBase:
    name: str
    _extensions: list

    @classmethod
    def extensions(cls):
        return cls._extensions + [
            ext.upper()
            for ext
            in cls._extensions
        ]


class ImageExtensions(ExtensionsBase):
    name = "image"
    _extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".tiff",
        ".tif",
        ".svg",
        ".svgz"
    ]


class VideoExtensions(ExtensionsBase):
    name = "video"
    _extensions = [
        ".mp4",
        ".mov",
        ".m4v",
        ".webm",
        ".avi",
        ".wmv",
        ".flv",
        ".mkv",
        ".ts"
    ]


if __name__ == '__main__':
    print(ImageExtensions.name, ImageExtensions.extensions(), sep=" ")
