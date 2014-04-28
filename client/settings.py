# if you change the persona, you also have to recompile the dictionary files
# https://github.com/jasperproject/jasper-client/issues/8
persona = "JASPER"

# microphone 
# run "arecord -l" to determine card #, subdevice#
input = {
  "device": "hw:0,0"
}

# speakers
# run "aplay -l" to determine card #, subdevice#
output = {
  "device": "hw:0,0"
}

commands = {
  "play": "aplay -D plug{device} %s".format(**output)
}
