import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones"

# List the fields in the ecozone shapefile
fields = arcpy.ListFields("C:\Users\91897\OneDrive\Desktop\EG Sem 1\Geo 115\ecozone_shp (1)\Ecozones\ecozones.shp")

# Print the field names
field_names = [field.name for field in fields]
print("Field Names:", field_names)


import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones"

# List the fields in the ecozone shapefile
fields = arcpy.ListFields("C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones/ecozones.shp")

# Print the field names
field_names = [field.name for field in fields]
print("Field Names:", field_names)


# Path to your ecozones shapefile
shapefile_path = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones/ecozones.shp"

# Initialize an empty dictionary
ecozones = {}

# Read the attribute table and extract relevant fields
with arcpy.da.SearchCursor(shapefile_path, ["ZONE_NAME", "ZONE_ID", "AREA"]) as cursor:
    for row in cursor:
        zone_name, zone_id, area = row
        ecozones[zone_name] = {"ZONE_ID": zone_id, "AREA": area}

# Now 'ecozones' contains the desired information
print(ecozones)



import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones"

# Specify the ZONE_ID to create a buffer for
zone_id = 1  # Change this to any ZONE_ID you want

# Create a feature layer for the specific ZONE_ID
arcpy.MakeFeatureLayer_management("C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones/ecozones.shp", "zone_layer", f"ZONE_ID = {zone_id}")

# Perform buffer analysis on the selected polygon
output_fc = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones/ecozones_buffer.shp"
arcpy.Buffer_analysis("zone_layer", output_fc, "100 Kilometers")

# Print a message indicating the buffer analysis is complete
print(f"Buffer analysis complete. Output saved as {output_fc}")


import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones"

# Add a new field to the ecozone feature class
input_fc = "C:/Users/91897/OneDrive/Desktop/EG Sem 1/Geo 115/ecozone_shp (1)/Ecozones/ecozones.shp"
new_field_name = "STUDENT_NM"
arcpy.AddField_management(input_fc, new_field_name, "TEXT")

# Populate the new field with the student's full name
student_name = "Uma Uvs"  # Replace with your full name
with arcpy.da.UpdateCursor(input_fc, [new_field_name]) as cursor:
    for row in cursor:
        row[0] = student_name
        cursor.updateRow(row)

# Print a message indicating the field has been added and populated
print(f"Field '{new_field_name}' added and populated with {student_name} in {input_fc}")



