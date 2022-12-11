MainWindowStyle = "background: QLinearGradient(x1: 0, y1: 0.5," \
                  "x2: 1, y2: 0.5," \
                  "stop: 0   rgb(0,90,170)," \
                  "stop: 0.75 rgb(171, 58, 141)," \
                  "stop: 1   rgb(231, 43, 112));"

poisk_formStyle = "QLineEdit {text-align: center;" \
                  "color: white;" \
                  "background: rgba(253, 254,255,0);" \
                  "border: 2px solid white;" \
                  "background-color: rgba(253, 254,255,0);}" \
                  "QLineEdit::createStandardContextMenu{" \
                  "background-color: rgba(253, 254,255,255);" \
                  "background: rgba(253, 254,255,255);" \
                  "border: 2px solid white;" \
                  "}}"

poisk_formStyleTeach = "QLineEdit {text-align: center;" \
                       "color: white;" \
                       "background: rgba(253, 254,255,0);" \
                       "border: 2px solid white;" \
                       "background-color: rgba(253, 254,255,0)}" \
                       "QLineEdit::createStandardContextMenu{" \
                       "background-color: rgba(253, 254,255,255);" \
                       "background: rgba(253, 254,255,255);" \
                       "border: 2px solid white;" \
                       "}}"

ProgressBarStyle = "QProgressBar" \
                   "{border-color: rgba(253, 254, 255,0);" \
                   "background-color: rgba(253, 254, 255,0);}" \
                   "QProgressBar::chunk{" \
                   "background-color: white;}"

str_under_poiskStyle = "background: none;" \
                       "color: white;"

str_types_of_weeksStyle = "background: none;" \
                          "color: white;"

TextEditStyle = "background-color:  rgba(0,0,0,0);" \
                "color: rgb(253, 254, 255);" \
                "outline: 0;" \
                "border: none;" \
                "outline: none;"

TextEditStyle2 = "border-top: 2px dashed rgba(255,255,255,0.3); " \
                 "color: rgb(253, 254, 255); "

OddWeekStyle = "<span style=\"  color:#ff0000;\" >" + "▲ </span>" + \
               "- верхняя (нечетная) неделя &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;▼ " \
               "- нижняя (четная) неделя"

EvenWeekStyle = "▲ - верхняя (нечетная) неделя &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" \
                + "<span style=\"  color:#18305c;\" >▼ </span>" + "- нижняя (четная) неделя"

labelStyle = "background: none;" \
             "color: white;" \
             "background: none;" \
             "border: none;"

FrameStyle = "background: rgb(0,97,181);" \
             "color: white;" \
             "border: 1px solid rgba(0,79,148,1);"

MenuButtonStyle = "QPushButton {background-color: rgba(255,0,255,0); " \
                  "image: url(images/menu.png) ;" \
                  "background-size: 100% 100%;}" \
                  "QPushButton:hover {" \
                  "image: url(images/menu_hover.png) ;}" \
                  "QPushButton:pressed {" \
                  "image: url(images/menu_pressed.png);}"

MenuButtonStyleLite = "QPushButton {background-color: rgba(255,0,255,0); " \
                      "color: rgba(255,255,255,150);" \
                      "font-family: Roboto;" \
                      "font-weight: bold;" \
                      "font-size: 32px;" \
                      "background-size: 100% 100%;}" \
                      "QPushButton:hover {color: rgba(255,255,255,255);}" \
                      "QPushButton:pressed {color: rgb(171, 58, 141);}"

CloseButtonStyle = "QPushButton {background-color: rgba(255,0,255,0); " \
                   "image: url(images/close.png) ;" \
                   "background-size: 100% 100%;" \
                   "border: none}" \
                   "QPushButton:hover {" \
                   "image: url(images/close_hover.png) ;}" \
                   "QPushButton:pressed {" \
                   "image: url(images/close_pressed.png);}"

CloseButtonStyleLite = "QPushButton {background-color: rgba(255,0,255,0); " \
                       "color: rgba(255,255,255,150);" \
                       "font-family: Roboto;" \
                       "font-weight: bold;" \
                       "font-size: 32px;" \
                       "background-size: 100% 100%;" \
                       "border: none}" \
                       "QPushButton:hover {color: rgba(255,255,255,255);}" \
                       "QPushButton:pressed {color: rgb(171, 58, 141);}"

SearchButtonsStyle = "QPushButton {font-family: Roboto;" \
                     "font-weight: bold;" \
                     "font-size: 14px;" \
                     "background: rgb(0, 90, 170);}" \
                     "QPushButton:hover {" \
                     "background: rgba(231, 43, 112,0.5);}" \
                     "QPushButton:pressed {" \
                     "background: rgba(231, 43, 112,0.7)};"

SearchButtonsStyleActive = "QPushButton {font-family: Roboto;" \
                           "font-weight: bold;" \
                           "font-size: 14px;" \
                           "background: rgb(0, 90, 170);" \
                           "border: 1px solid rgba(255,255,255,1);}" \
                           "QPushButton:hover {" \
                           "background: rgba(231, 43, 112,0.5);}" \
                           "QPushButton:pressed {" \
                           "background: rgba(231, 43, 112,0.7)};"

QScrollBarStyle = """
 /* --------------------------------------- QScrollBar  -----------------------------------*/
 QScrollBar:horizontal
 {
     background: rgba(200,200,200,0.1); 
 }

 QScrollBar::handle:horizontal
 {
     background: rgba(200,200,200,0.1);  
 }

 QScrollBar:vertical
 {
     background: rgba(200,200,200,0);
     width: 5px;
     margin: 0;

 }

 QScrollBar::handle:vertical
 {
     background-color: rgb(253,254,255);         
     border-radius: 4px;

 }

 QScrollBar::sub-line:vertical
 {
     height: 10px;
     width: 10px;
     subcontrol-position: top;
     subcontrol-origin: margin;
     background-color: rgb(232,94,147);
 }

 QScrollBar::add-line:vertical
 {     
     height: 10px;
     width: 10px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
 {              
     height: 10px;
     width: 10px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }

 QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
 {               
     height: 300px;
     width: 300px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
 {
     background: rgb(232,94,147);
 }
"""
