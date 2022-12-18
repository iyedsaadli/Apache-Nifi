from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import re

# Define a subclass of StreamCallback for use in session.write()
class PyStreamCallback(StreamCallback):
  def __init__(self):
        pass
  def process(self, inputStream, outputStream):
    text = IOUtils.toString(inputStream, StandardCharsets.ISO_8859_1)
    # regex out invalid escapes -- WORKS
    # new_text = re.sub(r"x03", "", text)
    new_text = text.replace("\x03", "")
    outputStream.write(new_text)
# end class
flowFile = session.get()
if(flowFile != None):
    try:
        flowFile = session.write(flowFile, PyStreamCallback())
        session.transfer(flowFile, REL_SUCCESS)
    except Exception as e:
        log.error('Something went wrong', e)
        session.transfer(flowFile, REL_FAILURE)
