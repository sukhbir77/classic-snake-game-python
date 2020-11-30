import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(name = "Snake Game",

                options = {
                    "build_exe" : {

                        "packages" : ["pygame"],
                        "include_files" : ["apple.png","snakehead.png","body.png","background.png","snakebg.jpg"]

                    }
                },

                description = "Snake Game : Funny Game",
                executables = executables



                )