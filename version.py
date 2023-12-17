class Version:
    PROJECT_NAME = "Ersoy Kardesler Win32 Subsystem"
    VERSION = "0.0.0"

    def get_project_name():
        with open("PROJECT_NAME", "r") as f:
            return f.readline().strip()

    def get_version():
        with open("VERSION", "r") as f:
            return f.readline().strip()


