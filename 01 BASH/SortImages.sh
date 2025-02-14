#!/bin/bash

# Verifica si dialog y exiftool están instalados
if ! command -v dialog &> /dev/null; then
    echo "dialog no está instalado. Por favor, instálalo para continuar."
    exit 1
fi

if ! command -v exiftool &> /dev/null; then
    echo "exiftool no está instalado. Por favor, instálalo para continuar."
    exit 1
fi

# Función para seleccionar carpeta usando dialog
function seleccionar_carpeta() {
    local prompt="$1"
    local result=$(dialog --stdout --title "$prompt" --dselect $HOME/ 14 48)
    
    if [ $? -eq 1 ]; then
        echo "Operación cancelada."
        exit 1
    fi
    
    echo "$result"
}

# Selección de carpetas usando dialog
source_folder=$(seleccionar_carpeta "Selecciona la carpeta de origen (fotos originales)")
destination_folder=$(seleccionar_carpeta "Selecciona la carpeta de destino (donde organizar las fotos)")

# Confirmación de las rutas seleccionadas
dialog --title "Confirmación" --yesno "Origen: $source_folder\nDestino: $destination_folder\n¿Es correcto?" 7 60
if [ $? -ne 0 ]; then
    echo "Operación cancelada."
    exit 1
fi

# Crea la estructura de carpetas organizadas por Año/Mes
echo "Organizando fotos desde $source_folder hacia $destination_folder"

# Función para organizar las fotos
function organizar_foto() {
    local file="$1"

    # Primero intenta mover basándose en los metadatos EXIF DateTimeOriginal
    exiftool '-Directory<DateTimeOriginal' -d "$destination_folder/%Y/%m" "$file"

    # Si no hay metadatos EXIF, usa FileModifyDate
    exiftool '-Directory<FileModifyDate' -d "$destination_folder/%Y/%m" "$file"

    # Si no hay metadatos, usa el nombre del archivo para determinar la fecha
    filename=$(basename "$file")
    if [[ "$filename" =~ ([0-9]{4})([0-9]{2})([0-9]{2}) ]]; then
        year=${BASH_REMATCH[1]}
        month=${BASH_REMATCH[2]}
        # Crear carpeta destino basada en el nombre del archivo
        target_folder="$destination_folder/$year/$month"
        mkdir -p "$target_folder"
        mv "$file" "$target_folder/"
        echo "Moviendo $filename a $target_folder"
    fi
}

# Recorre recursivamente todas las carpetas y archivos
find "$source_folder" -type f | while read -r file; do
    organizar_foto "$file"
done

# Mensaje final
dialog --msgbox "Organización completada. Las fotos se han movido a $destination_folder" 6 50
