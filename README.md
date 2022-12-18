# Apache-Nifi
The ExecuteScript Processor provides the ability to use a scripting language in order to leverage the NiFi API to perform tasks such as the following:

Read content and/or attributes from an incoming FlowFile
Create a new FlowFile (with or without a parent)
Write content and/or attributes to an outgoing FlowFile
Interact with the ProcessSession to transfer FlowFiles to relationships
Read/write to the State Manager to keep track of variables across executions of the processor
Notes:

The engine listed as "python" in the list of available script engines is actually Jython, not Python. When using Jython, you cannot import pure (CPython) modules such as pandas
