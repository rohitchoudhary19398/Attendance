class FileStatus:
    NOTSTARTED: str = "Not Started"
    RUNNING: str = "Running"
    PROCESSED: str = "Processed"
    ALL: list = [NOTSTARTED, RUNNING, PROCESSED]


class FileType:
    PDF = "pdf"
    CSV = "csv"
    ZIP = "zip"

    file_map = {
        "application/pdf": PDF,
        "application/csv": CSV,
        "application/zip": ZIP,
    }

    @classmethod
    def get_file_type(cls, content_type: str):
        return cls.file_map.get(content_type, None)

    @classmethod
    def get_file_type_from_name(cls, name: str):
        if cls.is_pdf(name):
            return cls.PDF
        elif cls.is_zip(name):
            return cls.ZIP
        return None

    @classmethod
    def is_pdf(cls, content_type: str):
        return cls.get_file_type(
            content_type
        ) == cls.PDF or content_type.lower().endswith(cls.PDF)

    @classmethod
    def is_zip(cls, content_type: str):
        return cls.get_file_type(
            content_type
        ) == cls.ZIP or content_type.lower().endswith(cls.ZIP)
