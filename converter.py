file_name=input("Input filename with extension: ") #input filename with extension 
raw_data = open(file_name, "r")  #reads data from file to a handle, file must be in the same directory as the code
raw_string = raw_data.read() #reads data from handle to a string
remove_newline=raw_string.replace('\n','') #removes any existing newline character 
newline = remove_newline.replace(',', '\n') #replaces commas in the data with a newline character
final = newline.replace(' ', '') #removes whitespace from data
file_output=open('output.txt', 'w') #creates a file 'output.txt' assigns file_output handle to it to write data
file_output.write(final) #appends the content of final to file_output
file_output.close() #closes the handle
