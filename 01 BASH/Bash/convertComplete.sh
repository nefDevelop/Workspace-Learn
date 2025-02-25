#!/bin/bash

# Carpeta donde están las fuentes
DIRECTORIO_FUENTES="./"
# Archivo CSS de salida
ARCHIVO_CSS="./fuentes_embed.css"

# Limpia el archivo CSS anterior
echo "/* Fuentes embebidas en base64 */" > "$ARCHIVO_CSS"

# Procesar cada archivo .woff2
for FUENTE in "$DIRECTORIO_FUENTES"/*.woff2; do
    # Obtener el nombre del archivo sin la ruta
    NOMBRE_ARCHIVO=$(basename "$FUENTE" .woff2)

    # Extraer metadatos de la fuente
    METADATOS=$(ttx -o - -t fvar "$FUENTE" 2>/dev/null)
#	echo "$METADATOS"
#   Extraer instancias nombradas
#   minValue=$(echo "$METADATOS" | grep -oP '<MinValue>.*?</MinValue>')
#	maxValue=$(echo "$METADATOS" | grep -oP '<MaxValue>.*?</MaxValue>')
#	defValue=$(echo "$METADATOS" | grep -oP '<DefaultValue>.*?</DefaultValue>')

	minValue=$(echo "$METADATOS" | grep -oP '(?<=<MinValue>).*?(?=</MinValue>)' | sed 's/\.0$//') 
	maxValue=$(echo "$METADATOS" | grep -oP '(?<=<MaxValue>).*?(?=</MaxValue>)' | sed 's/\.0$//')
	defValue=$(echo "$METADATOS" | grep -oP '(?<=<DefaultValue>).*?(?=</DefaultValue>)' | sed 's/\.0$//')


    # Detectar estilo (normal o italic)
    if [[ "$METADATOS" =~ Italic ]]; then
        FONT_STYLE="italic"
    else
        FONT_STYLE="normal"
    fi


    # Procesar cada NamedInstance
   # while read -r $METADATOS; do
        # Detectar estilo (normal o italic)
        # if [[ "$INSTANCIA" =~ Italic ]]; then
        #     FONT_STYLE="italic"
        # else
        #     FONT_STYLE="normal"
        # fi

        # Detectar peso (wght)
        if [[ -n "$minValue" && -n "$maxValue" && "$minValue" -gt 0 && "$maxValue" -gt 0 ]]; then
            FONT_WEIGHT="$minValue $maxValue"
        else
            if [[-n "$defValue" && "$defValue" -gt 0]]; then
                FONT_WEIGHT="$defValue"
            else
                FONT_WEIGHT="500"
            fi
        fi

        echo "FONT_WEIGHT=$FONT_WEIGHT"

        # Codificar la fuente en base64
        MIME_TYPE="application/font-woff2"
        BASE64_ENCODED=$(base64 -w 0 "$FUENTE")

        # Añadir la definición @font-face al archivo CSS
        echo "@font-face {
            font-family: '$NOMBRE_ARCHIVO';
            font-style: $FONT_STYLE;
            font-weight: $FONT_WEIGHT;
            font-stretch: normal;
            font-display: swap;
            src: url('data:$MIME_TYPE;base64,$BASE64_ENCODED') format('woff2');
        }" >> "$ARCHIVO_CSS"

        echo "Fuente $NOMBRE_ARCHIVO añadida al archivo CSS con:
              - Estilo: $FONT_STYLE
              - Peso: $FONT_WEIGHT"
    #done <<< "$INSTANCIAS"
done

echo "CSS completo generado en $ARCHIVO_CSS."
