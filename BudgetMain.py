from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_string("""

<BestView>:
    spacing: "5dp"
	padding: "5dp"
    tab_pos: "top_left"
	do_default_tab: False
	tab_height: "50dp"
	tab_width: root.width/3
    do_default_tab: False

    TabbedPanelItem:
        text: 'Welcome'
        Label:
            text: 'First tab content area'
    TabbedPanelItem:
        text: 'View'
        BoxLayout:
            ListView:
                item_strings: [str(index) for index in range(100)]

    TabbedPanelItem:
        text: 'Add'
        BoxLayout:
            spacing: "1dp"
	        padding: "1dp"
            orientation:"vertical"
            Label:
                height: "50dp"
                font_size: "16dp"
                text: 'Please Enter The Amount,Time and Date'
            BoxLayout:
                Label:
                    height: "20dp"
                    text:"Amount:"
                    size_hint_x:"0.25"
                    size_hint_y:"0.50"
                TextInput:
                    height: "20dp"
                    size_hint_x:"0.25"
                    size_hint_y:"0.50"
                    multiline:False
            BoxLayout:
                Label:
                    height: "20dp"
                    text:"Date:"
                    size_hint_x:"0.25"
                    size_hint_y:"0.50"
                TextInput:
                    height: "20dp"
                    size_hint_x:"0.25"
                    size_hint_y:"0.50"
                    multiline:False
            BoxLayout:
                Label:
                    text:"Type:"
                    height: "20dp"
                    size_hint_x:"0.25"
                    size_hint_y:"0.50"
                TextInput:
                    height: "20dp"
                    size_hint_x:"0.25"
                    size_hint_y:"0.50"
                    multiline:False
            AnchorLayout:
                spacing: "1dp"
	            padding: "1dp"
                anchor_x:"right"
                anchor_y:"bottom"
                Button:
		            text: "Submit"
		            size_hint_x:0.20
		            size_hint_y:"0.35"
		            halign: "right"
		            on_release: app.add_transaction()





""")


class BestView(TabbedPanel):
    pass


class BudgetApp(App):
    def build(self):
        return BestView()


if __name__ == '__main__':
    BudgetApp().run()