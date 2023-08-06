# © 2022 George Fenn
# Original name was my_utils, but that was changed to handie_utils 
# for distribution purposes.
# V2 Changed to use a pyui user interface to indicate utility
# choice.
# V3 Added a background display. This is done by running a quick look
# of the image file in the background. The name of this image file is 
# acquired from the new parameter file written by V3 of handie_install_util.

import dialogs
from SOTA_summit_lookup import main as SOTA_util
from POTA_park_lookup import main as POTA_util
from lat_long_distance_calculate import main as calculate
from dms_convert_frontend import main as convert
from QRZ_XML_frontend import main as qrz_call
import ui
import console
import csv
from threading import Thread
import sys

class my_file_context:
  
  def __init__(self):
    self.debug=0
  def __enter__(self):
    try:
      self.file = open('handie_param.csv')
      return self.file
    except FileNotFoundError:
      i=dialogs.alert('\n Parameter file not found!','','OK',hide_cancel_button=True)
    except IOError as err:
      i=dialogs.alert(err,'','OK',hide_cancel_button=True)
    
  def __exit__(self, type, value, traceback):
    if all((type, value, traceback)):
      if self.debug:
        i=dialogs.alert(f'Type: {type} Value: {value} Traceback: {traceback}','','OK',hide_cancel_button=True)
      sys.exit()
    else:
      self.file.close()
      
def show_background():
  
  with my_file_context() as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    row=(next(csv_reader))
    background_file=row['Background']
    
  console.quicklook(background_file)

def main():
  
  def park_button_pressed(sender):
    v.close()
    v.choices=POTA
    
  def summit_button_pressed(sender):
    v.close()
    v.choices=SOTA
    
  def calculate_button_pressed(sender):
    v.close()
    v.choices=calc
    
  def convert_button_pressed(sender):
    v.close()
    v.choices=dms_dd
    
  def callsign_button_pressed(sender):
    v.close()
    v.choices=qrz_lookup
    
  def handie_done_button_pressed(sender):
    v.close()
    v.done_button=True
  
  def handie_view_present():
    
    if min(ui.get_screen_size()) >= 768:
      # iPad
      v.frame = (0, 0, 360, 400)
      v.present('sheet')
    else:
      # iPhone
      v.present(orientations=['portrait'])
    v.wait_modal()
    
  v = ui.load_view('handie_utils_ui')
  v.done_button = ''
  
  POTA_list=[]
  SOTA_list=[]

  POTA='Park Lookup'
  SOTA='Summit Lookup'
  calc='Calculate Distance'
  dms_dd='Coordinates Conversion'
  qrz_lookup='Call Sign Lookup'
  
  while True:
    v.choices=''
    handie_view_present()

    if v.choices == '' or v.done_button == True:
      break
    elif v.choices == POTA:
      POTA_util(POTA_list)
    elif v.choices == SOTA:
      SOTA_util(SOTA_list)
    elif v.choices == calc:
      calculate()
    elif v.choices == dms_dd:
      convert()
    elif v.choices == qrz_lookup:
      try:
        qrz_call()
      except SystemExit:
        pass

# end of While True

if __name__ == "__main__":
  
  t = Thread(target=show_background)
  t.start()
    
  main()
