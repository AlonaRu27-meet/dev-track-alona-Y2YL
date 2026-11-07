import flet as ft


first = ft.TextField(label="Enter backround color:", color = "#FFFFFF", bgcolor="#FBDC40")
second = ft.TextField(label="Enter titles color:", color = "#FFFFFF", bgcolor="#B1FF81")
third = ft.TextField(label="Enter text boxes color:", color = "#FFFFFF", bgcolor="#90E9FF")
fourth = ft.TextField(label="Enter buttons color:", color = "#FFFFFF", bgcolor="#77A6FF")
title = ft.Text("Pallete Me", size = 50, color = "#3E280A")
subtitle = ft.Text("Create your own colorful combination!", size = 30, color = "#DE6464")
name = ft.TextField(label="Enter your name:", color = "#FFFFFF", bgcolor="#E7983E")
designs = []
def main(page: ft.Page):
    page.title = "Alona's app"
    page.bgcolor = "#FFE9C0"
    page.add(title)
    page.add(subtitle)
    page.add(name)
    page.add(first)
    page.add(second)
    page.add(third)
    page.add(fourth)

    def clicked(e: ft.Event[ft.Button]):
        design = ft.Button(name.value, bgcolor = "#DE61EE", color = "#FFFFFF", width=140, height=40, on_click= lambda e:load_design(new_design))
        page.show_dialog(ft.SnackBar(ft.Text("In process...")))
        page.bgcolor = first.value.strip()
        title.color = second.value.strip()
        subtitle.color = second.value.strip()
        first.bgcolor = third.value.strip()
        second.bgcolor = third.value.strip()
        third.bgcolor = third.value.strip()
        fourth.bgcolor = third.value.strip()
        name.bgcolor = third.value.strip()
        button.bgcolor = fourth.value.strip()
        design.bgcolor = fourth.value.strip()
        designs_title.color = second.value.strip()
        new_design = {"name": name.value, "bgcolor": first.value, "titles": second.value, "txt_boxes": third.value, "buttons": fourth.value}
        designs.append(new_design)
        if name.value.strip().lower() == "secret":
            page.show_dialog(ft.SnackBar(ft.Text("You discovered a secret design!")))
            new_design["bgcolor"] = "#35264B"
            new_design["titles"] = "#A477B8"
            new_design["txt_boxes"] = "#E9B8D0"
            new_design["buttons"] = "#F9E9F2"
            page.bgcolor = new_design["bgcolor"]
            title.color = new_design["titles"]
            subtitle.color = new_design["titles"]

            first.bgcolor = new_design["txt_boxes"]
            second.bgcolor = new_design["txt_boxes"]
            third.bgcolor = new_design["txt_boxes"]
            fourth.bgcolor = new_design["txt_boxes"]

            button.bgcolor = new_design["buttons"]
            name.bgcolor = new_design["txt_boxes"]
            button.bgcolor = new_design["buttons"]
            designs_title.color = new_design["titles"]
            design.bgcolor = new_design["buttons"]
        designs_list.controls.append(design)
        page.update()

    button = ft.Button("Create my design", bgcolor = "#BC91F5", color = "#FFFFFF", on_click= clicked)

    page.add(button)
    def load_design(dsn: ft):
        page.bgcolor = dsn["bgcolor"]
        title.color = dsn["titles"]
        subtitle.color = dsn["titles"]

        first.bgcolor = dsn["txt_boxes"]
        second.bgcolor = dsn["txt_boxes"]
        third.bgcolor = dsn["txt_boxes"]
        fourth.bgcolor = dsn["txt_boxes"]

        button.bgcolor = dsn["buttons"]
        page.update()
    designs_title = ft.Text("My Designs", size=30, weight=ft.FontWeight.BOLD, color="#FF85A1")
    designs_list = ft.ListView(width=200, height=600, spacing=8)
    page.add(designs_title)
    page.add(designs_list)


ft.run(main)
