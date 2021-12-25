import json
from sys import argv

class RealtimeSchedulingViewerSVG:
	OFFSET_X = 50
	OFFSET_Y = 10
	HEIGHT = 75
	WIDTH  = 5
	FONT_SIZE = HEIGHT/3
	WIDTH_UNIT = 500
	HEIGHT_UNIT = 250

	color_list = ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige","Bisque","Black","BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGreen","DarkGrey","DarkKhaki","DarkMagenta","DarkOliveGreen","Darkorange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DimGrey","DodgerBlue","FireBrick","FloralWhite","ForestGreen","Fuchsia","Gainsboro","GhostWhite","Gold","GoldenRod","Gray","Green","GreenYellow","Grey","HoneyDew","HotPink","IndianRed","Indigo","Ivory","Khaki","Lavender","LavenderBlush","LawnGreen","LemonChiffon","LightBlue","LightCoral","LightCyan","LightGoldenRodYello","LightGray","LightGreen","LightGrey","LightPink","LightSalmon","LightSeaGreen","LightSkyBlue","LightSlateGray","LightSlateGrey","LightSteelBlue","LightYellow","Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin","NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise","PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","SeaShell","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SlateGrey","Snow","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","White","WhiteSmoke","Yellow","YellowGreen"]

	def __init__(self, input_filename, output_filename):
		self.input_filename = input_filename
		self.output_filename = output_filename
		self.color_count = 0
		#self.color_hash = Hash.new

	def print_svg(self):
		json_file = open(self.input_filename)
		json_data = json.load(json_file)
		self.core_num = json_data["coreNum"]
		self.makespan = json_data["makespan"]

		self.write_header(self.makespan, self.core_num * RealtimeSchedulingViewerSVG.HEIGHT)
		self.draw_lines(self.makespan, self.core_num * RealtimeSchedulingViewerSVG.HEIGHT)
		"""
		data["taskSet"].each{|task|
		  	draw_task(task["coreID"].to_i, task["taskName"], task["startTime"].to_i, task["executionTime"].to_i)
		  }"""
		  #for test
		  #100.times{|i|
		#	draw_task(rand(10),"task_#{i}", rand(100), rand(500)+10)
		#  }
		self.write_script()
		self.write_footer()


	def draw_lines(self, height, width):
		output_file = open(self.output_filename, "a")
		n = int(width / RealtimeSchedulingViewerSVG.WIDTH_UNIT)
		for i in range(n):
			x = i * RealtimeSchedulingViewerSVG.WIDTH_UNIT + RealtimeSchedulingViewerSVG.OFFSET_X
			text_x = i * RealtimeSchedulingViewerSVG.WIDTH_UNIT

			output_file.write("\t\t<line id =\"line_"+str(text_x)+"\" class=\"selectable\" x1=\""+str(x)+"\" y1=\"0\" x2=\""+str(x)+"\" y2=\""+str(height)+"\" stroke-width=\"15\" stroke=\"black\" />\n")
			output_file.write("\t\t<text id =\"line_"+str(text_x)+"-info\" x=\""+str(x)+"\" y=\"100\"  font-family=\"Verdana\" font-size=\""+str(RealtimeSchedulingViewerSVG.FONT_SIZE * 2)+"\" stroke=\"blue\">\n")
			output_file.write(str(i * RealtimeSchedulingViewerSVG.WIDTH_UNIT / 10)+"/text>\n")
		"""
  			(height/HEIGHT_UNIT).times{|y|
  				#print "\t\t<text id =\"line_#{text_x}-info\" x=\"#{x}\" y=\"#{y*HEIGHT_UNIT}\"  font-family=\"Verdana\" font-size=\"#{FONT_SIZE*2}\" stroke=\"blue\" opacity=\"0.0\">"
  				print "\t\t<text id =\"line_#{text_x}-info\" x=\"#{x}\" y=\"#{y*HEIGHT_UNIT}\"  font-family=\"Verdana\" font-size=\"#{FONT_SIZE*2}\" stroke=\"blue\">"
  				puts  "#{i * WIDTH_UNIT / 10}</text>"
  			}
		"""

	"""
	def draw_task(core_id, task_name, start_time, exection_time)
		p @color_hash
		p @color_list
		p @color_count
		if @color_hash[task_name] == nil
			@color_hash[task_name] = @@color_list[@color_count] 
			@color_count = @color_count + 1
		end

		color = @color_hash[task_name]

		#puts  "\t\t<rect id =\"#{task_name}\" class=\"selectable\" x=\"#{start_time*WIDTH + OFFSET_X}\" y=\"#{core_id*HEIGHT + OFFSET_Y}\" width=\"#{exection_time*WIDTH}\" height=\"#{HEIGHT-10}\" stroke=\"black\" fill=\"white\" stroke-width=\"2\" />"
		puts  "\t\t<rect id =\"#{task_name}_#{start_time}\" class=\"selectable\" x=\"#{start_time*WIDTH + OFFSET_X}\" y=\"#{core_id*HEIGHT + OFFSET_Y}\" width=\"#{exection_time*WIDTH}\" height=\"#{HEIGHT-10}\" stroke=\"black\" fill=\"#{color}\" stroke-width=\"2\" />"
		puts  "\t\t<text id =\"#{task_name}_#{start_time}\" class=\"selectable\" x=\"#{start_time*WIDTH + OFFSET_X}\" y=\"#{core_id*HEIGHT + OFFSET_Y+ FONT_SIZE}\"             width=\"#{exection_time*WIDTH + OFFSET_X}\" font-family=\"Verdana\" font-size=\"#{FONT_SIZE}\"> #{task_name} </text>"
		print "\t\t<text id =\"#{task_name}_#{start_time}-info\" x=\"#{start_time*WIDTH + OFFSET_X}\" y=\"#{core_id*HEIGHT + OFFSET_Y + FONT_SIZE + HEIGHT/2}\" width=\"#{exection_time*WIDTH + OFFSET_X}\" font-family=\"Verdana\" font-size=\"#{FONT_SIZE}\" stroke=\"blue\" opacity=\"0.0\">"
		#puts  "#{task_name}@#{core_id}:#{start_time}~#{start_time+exection_time}</text>"
		puts  "#{start_time}~#{start_time+exection_time}@#{core_id}</text>"
	end"""

	def print_style(self):
		output_file = open(self.output_filename, "a")
		output_file.write("\t<style>\n")
		output_file.write("\t.selectable:hover {\n")
		output_file.write("\t\tfill: orange;\n")
		output_file.write("\t\tstroke: orange;\n")
		output_file.write("\t}\n")
		output_file.write("\t.shown {\n")
		output_file.write("\t\topacity: 1;\n")
		output_file.write("\t}\n")
		output_file.write("\t</style>\n")
		output_file.close()

	def write_header(self, height, width):
		output_file = open(self.output_filename, "w")
		output_file.write("<html>\n")
		output_file.write("\t<body>\n")
		output_file.close()

		self.print_style()
		
		output_file = open(self.output_filename, "a")
		output_file.write("\t<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n")
		#puts "\t<svg width=\"#{width}\" height=\"#{height}\"  xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">"
		output_file.write("\t<svg width=\""+str(width)+"\" height=\""+str(height)+"\" viewBox=\"0 0 "+str(height)+" "+str(width)+"\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
		output_file.close()

	def write_script(self):
		output_file = open(self.output_filename, "a")
		output_file.write("\t\t\t<script>\n")
		output_file.write("\t\t\tlet selectableElements = document.getElementsByClassName(\"selectable\");\n")
		output_file.write("\t\t\tArray.from( selectableElements ).forEach(elem => {\n")
		output_file.write("\t\t\t\telem.addEventListener(\"mouseover\", eve => {\n")
		output_file.write("\t\t\t\t\tlet textId = elem.id + \"-info\";\n")
		output_file.write("\t\t\t\t\tlet textElem = document.getElementById(textId);\n")
		output_file.write("\t\t\t\t\tif( textElem != null ) {\n")
		output_file.write("\t\t\t\t\t\ttextElem.classList.add(\"shown\");\n")
		output_file.write("\t\t\t\t\t}\n")
		output_file.write("\t\t\t\t});\n")
		output_file.write("\t\t\t\telem.addEventListener(\"mouseleave\", eve => {\n")
		output_file.write("\t\t\t\t\tlet textId = elem.id + \"-info\";\n")
		output_file.write("\t\t\t\t\tlet textElem = document.getElementById(textId);\n")
		output_file.write("\t\t\t\t\tif( textElem != null ) {\n")
		output_file.write("\t\t\t\t\t\ttextElem.classList.remove(\"shown\");\n")
		output_file.write("\t\t\t\t\t}\n")
		output_file.write("\t\t\t\t});\n")
		output_file.write("\t\t\t});\n")
		output_file.write("\t\t\t</script>\n")
		output_file.close()

	def write_footer(self):
		output_file = open(self.output_filename, "a")
		output_file.write("\t\t</svg>\n")
		output_file.write("\t</body>\n")
		output_file.write("</html>\n")
		output_file.close()

"""
opt = OptionParser.new

opt.on('-o') {|v| puts "test #{v}" }
opt.on('--[no-]bar') {|v| p v }
opt.parse!(ARGV)
p ARGV
"""

input_file = argv[1] if len(argv) > 1 else "sample.json"
output_file = argv[2] if len(argv) > 2 else "output.html"

print("input_file : "+input_file)
print("output_file: "+output_file)
svg_viewer = RealtimeSchedulingViewerSVG(input_file, output_file)
svg_viewer.print_svg()


"""
print_header(10000, $core_num * HEIGHT)

draw_task(1, "task1", 0, 10)
draw_task(2, "task2", 0, 20)

100.times{|i|
	draw_task(rand(10),"task_#{i}", rand(100), rand(500)+10)
}

print_script()
print_footer()
"""