import datetime
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from python_sqlite import data_handler
from kivy.uix.popup import Popup

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
        FloatLayout:
            Image:
                source: "images/main_bg.jpg"
                allow_stretch: True
                keep_ratio: False
                size_hint: 1, 1
            Label:
                text:"Welcome To Budget App"
                color: 1,0,0,1
                size:self.size
    TabbedPanelItem:
        text: 'View'
        id:view_tab
        on_release: app.view_transaction(output_trans)
        BoxLayout:
            orientation: 'vertical'
            PageLayout:
                ScrollView: 
                    Label:
                        id:output_trans
                        text: ''
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_y: None
                        halign: 'center'
                       
        
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
                    id:input_amount
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
                    id:input_date
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
                    id:input_ttype
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
		            on_release: app.add_transaction(input_amount.text,input_date.text,input_ttype.text)


""")


class BestView(TabbedPanel):
    pass


class BudgetApp(App):
    def build(self):
        return BestView()


    def add_transaction(self, amount, date, ttype):
        print "INFO:Function add_transaction Caled" + str(amount) + str(date) + str(ttype)
        d_h=data_handler()
        d_h.add_trans(str(amount),str(date),str(ttype))
        trans=d_h.view_trans()

    def view_transaction(self,output_trans):
        print "INFO:view_transaction called"
        d_h = data_handler()
        #d_h.add_trans(str(amount), str(date), str(ttype))
        trans = d_h.view_trans()
        print trans
        output_trans.text=str(trans)
        #return d_h.view_trans()

    def Picker(self):
        self.laDate = self.datepicker.text
        self.datepicked = datetime.datetime.strptime(self.laDate, '%d.%m.%Y').strftime('%d/%m/%Y')
        self.myLabel.text = str(self.datepicked)

if __name__ == '__main__':
    BudgetApp().run()
