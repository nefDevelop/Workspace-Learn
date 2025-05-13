package main

import (
	"fmt"
	"strings"

	"github.com/charmbracelet/bubbles/key"
	"github.com/charmbracelet/bubbles/list"
	"github.com/charmbracelet/bubbles/viewport"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

// Define estilos
var (
	// Estilos base para los paneles
	borderStyle = lipgloss.NewStyle().
			BorderStyle(lipgloss.RoundedBorder()).
			BorderForeground(lipgloss.Color("63")).
			Padding(0, 1)

	// Estilo para panel activo
	activeStyle = lipgloss.NewStyle().
			BorderStyle(lipgloss.RoundedBorder()).
			BorderForeground(lipgloss.Color("205")).
			Padding(0, 1)

	// Estilo para ventanas modales
	modalStyle = lipgloss.NewStyle().
			BorderStyle(lipgloss.DoubleBorder()).
			BorderForeground(lipgloss.Color("170")).
			Padding(1, 2).
			Background(lipgloss.Color("237"))

	// Estilos para los títulos
	titleStyle = lipgloss.NewStyle().
			Bold(true).
			Foreground(lipgloss.Color("205"))

	// Estilos para botones en modales
	buttonStyle = lipgloss.NewStyle().
			Foreground(lipgloss.Color("0")).
			Background(lipgloss.Color("63")).
			Padding(0, 3).
			MarginRight(1)

	// Estilo para botón seleccionado
	selectedButtonStyle = lipgloss.NewStyle().
				Foreground(lipgloss.Color("0")).
				Background(lipgloss.Color("205")).
				Padding(0, 3).
				MarginRight(1)
)

// Item para las listas de archivos
type fileItem struct {
	name        string
	path        string
	isDirectory bool
}

func (i fileItem) Title() string {
	if i.isDirectory {
		return "📁 " + i.name
	}
	return "📄 " + i.name
}

func (i fileItem) Description() string {
	return i.path
}

func (i fileItem) FilterValue() string {
	return i.name
}

// Teclados personalizados
type keyMap struct {
	Up    key.Binding
	Down  key.Binding
	Left  key.Binding
	Right key.Binding
	Tab   key.Binding
	Copy  key.Binding
	Move  key.Binding
	Paste key.Binding
	Quit  key.Binding
	Enter key.Binding
	Esc   key.Binding
}

var keys = keyMap{
	Up: key.NewBinding(
		key.WithKeys("up", "k"),
		key.WithHelp("↑/k", "arriba"),
	),
	Down: key.NewBinding(
		key.WithKeys("down", "j"),
		key.WithHelp("↓/j", "abajo"),
	),
	Left: key.NewBinding(
		key.WithKeys("left", "h"),
		key.WithHelp("←/h", "izquierda"),
	),
	Right: key.NewBinding(
		key.WithKeys("right", "l"),
		key.WithHelp("→/l", "derecha"),
	),
	Tab: key.NewBinding(
		key.WithKeys("tab"),
		key.WithHelp("tab", "cambiar panel"),
	),
	Copy: key.NewBinding(
		key.WithKeys("c"),
		key.WithHelp("c", "copiar"),
	),
	Move: key.NewBinding(
		key.WithKeys("m"),
		key.WithHelp("m", "mover"),
	),
	Paste: key.NewBinding(
		key.WithKeys("p"),
		key.WithHelp("p", "pegar"),
	),
	Quit: key.NewBinding(
		key.WithKeys("q", "ctrl+c"),
		key.WithHelp("q", "salir"),
	),
	Enter: key.NewBinding(
		key.WithKeys("enter"),
		key.WithHelp("enter", "seleccionar"),
	),
	Esc: key.NewBinding(
		key.WithKeys("esc"),
		key.WithHelp("esc", "cancelar"),
	),
}

// Tipo de ventana modal
type modalType int

const (
	copyModal modalType = iota
	moveModal
	pasteModal
	noModal
)

// Modelo principal
type model struct {
	panels           []list.Model   // Paneles principales (3 paneles)
	activePanel      int            // Índice del panel activo
	viewport         viewport.Model // Para mostrar contenido de archivo
	width            int            // Ancho de la terminal
	height           int            // Alto de la terminal
	showModal        bool           // Si hay una ventana modal visible
	modalType        modalType      // Tipo de modal activo
	modalContent     string         // Contenido de la modal
	modalTitle       string         // Título de la modal
	modalSelectedBtn int            // Botón seleccionado en la modal
	modalButtons     []string       // Botones en la modal
	modalList        list.Model     // Lista para seleccionar archivos en modal
	selectedItem     *fileItem      // Archivo seleccionado actualmente
	clipboard        *fileItem      // Archivo en el portapapeles
	clipboardAction  string         // Acción para el portapapeles (copiar/mover)
}

func initialModel() model {
	// Crear listas de ejemplo para cada panel
	panels := make([]list.Model, 3)

	// Datos de ejemplo para cada panel
	panelData := [][]fileItem{
		// Panel 1: Raíz
		{
			{name: "Documentos", path: "/home/user/Documentos", isDirectory: true},
			{name: "Descargas", path: "/home/user/Descargas", isDirectory: true},
			{name: "Imágenes", path: "/home/user/Imágenes", isDirectory: true},
			{name: "README.md", path: "/home/user/README.md", isDirectory: false},
			{name: "config.json", path: "/home/user/config.json", isDirectory: false},
		},
		// Panel 2: Documentos
		{
			{name: "Proyectos", path: "/home/user/Documentos/Proyectos", isDirectory: true},
			{name: "Personal", path: "/home/user/Documentos/Personal", isDirectory: true},
			{name: "informe.pdf", path: "/home/user/Documentos/informe.pdf", isDirectory: false},
			{name: "notas.txt", path: "/home/user/Documentos/notas.txt", isDirectory: false},
		},
		// Panel 3: Proyectos
		{
			{name: "Go", path: "/home/user/Documentos/Proyectos/Go", isDirectory: true},
			{name: "Python", path: "/home/user/Documentos/Proyectos/Python", isDirectory: true},
			{name: "app.go", path: "/home/user/Documentos/Proyectos/app.go", isDirectory: false},
			{name: "README.md", path: "/home/user/Documentos/Proyectos/README.md", isDirectory: false},
		},
	}

	// Configurar títulos y contenido para cada panel
	titles := []string{" / ", " Documentos ", " Proyectos "}

	for i := range panels {
		// Convertir fileItems a list.Items
		items := make([]list.Item, len(panelData[i]))
		for j, item := range panelData[i] {
			items[j] = item
		}

		// Crear lista con estilo personalizado
		l := list.New(items, list.NewDefaultDelegate(), 0, 0)
		l.Title = titles[i]
		l.SetShowHelp(false)
		panels[i] = l
	}

	// Crear vista para contenido de archivo
	vp := viewport.New(0, 0)
	vp.SetContent("Seleccione un archivo para ver su contenido...")

	// Crear lista para modales
	modalList := list.New([]list.Item{}, list.NewDefaultDelegate(), 0, 0)
	modalList.Title = "Seleccionar destino"
	modalList.SetShowHelp(false)

	return model{
		panels:           panels,
		activePanel:      0,
		viewport:         vp,
		showModal:        false,
		modalType:        noModal,
		modalButtons:     []string{"Aceptar", "Cancelar"},
		modalSelectedBtn: 0,
		modalList:        modalList,
	}
}

func (m model) Init() tea.Cmd {
	return nil
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	var cmds []tea.Cmd

	switch msg := msg.(type) {
	case tea.KeyMsg:
		// Si hay un modal abierto, manejar sus eventos primero
		if m.showModal {
			switch {
			case key.Matches(msg, keys.Esc):
				// Cerrar modal con Escape
				m.showModal = false
				return m, nil

			case key.Matches(msg, keys.Left), key.Matches(msg, keys.Right):
				// Navegar entre botones en el modal
				m.modalSelectedBtn = (m.modalSelectedBtn + 1) % len(m.modalButtons)
				return m, nil

			case key.Matches(msg, keys.Enter):
				if m.modalSelectedBtn == 0 { // Botón "Aceptar"
					// Procesamos la acción según el tipo de modal
					switch m.modalType {
					case copyModal, moveModal:
						// Guardar en portapapeles
						if sel, ok := m.panels[m.activePanel].SelectedItem().(fileItem); ok {
							m.clipboard = &sel
							if m.modalType == copyModal {
								m.clipboardAction = "copiar"
							} else {
								m.clipboardAction = "mover"
							}
						}
					case pasteModal:
						// Ejecutar acción de pegar
						if m.clipboard != nil {
							// Aquí se implementaría la lógica real para copiar/mover
							// Por ahora solo mostramos mensaje de éxito
							action := "copiado"
							if m.clipboardAction == "mover" {
								action = "movido"
							}
							m.modalContent = fmt.Sprintf("%s %s a la ubicación actual",
								m.clipboard.name, action)
						}
					}
				}
				// Cerrar modal en ambos casos (Aceptar o Cancelar)
				m.showModal = false
				return m, nil

			case key.Matches(msg, keys.Up), key.Matches(msg, keys.Down):
				// Si hay una lista en el modal, actualizar la lista
				if m.modalType == pasteModal {
					var cmd tea.Cmd
					m.modalList, cmd = m.modalList.Update(msg)
					return m, cmd
				}
			}

			// Si tenemos un modal con lista, procesar sus eventos
			if m.modalType == pasteModal {
				var cmd tea.Cmd
				m.modalList, cmd = m.modalList.Update(msg)
				return m, cmd
			}

			return m, nil
		}

		// Gestión normal de teclas (sin modales)
		switch {
		case key.Matches(msg, keys.Quit):
			return m, tea.Quit

		case key.Matches(msg, keys.Tab):
			// Cambiar panel activo
			m.activePanel = (m.activePanel + 1) % len(m.panels)

		case key.Matches(msg, keys.Copy):
			// Mostrar modal de copiar
			m.showModal = true
			m.modalType = copyModal
			m.modalTitle = "Copiar archivo"
			if sel, ok := m.panels[m.activePanel].SelectedItem().(fileItem); ok {
				m.modalContent = fmt.Sprintf("¿Desea copiar \"%s\"?", sel.name)
			} else {
				m.modalContent = "Seleccione un archivo para copiar"
			}

		case key.Matches(msg, keys.Move):
			// Mostrar modal de mover
			m.showModal = true
			m.modalType = moveModal
			m.modalTitle = "Mover archivo"
			if sel, ok := m.panels[m.activePanel].SelectedItem().(fileItem); ok {
				m.modalContent = fmt.Sprintf("¿Desea mover \"%s\"?", sel.name)
			} else {
				m.modalContent = "Seleccione un archivo para mover"
			}

		case key.Matches(msg, keys.Paste):
			// Mostrar modal de pegar
			if m.clipboard != nil {
				m.showModal = true
				m.modalType = pasteModal
				m.modalTitle = fmt.Sprintf("%s archivo",
					strings.Title(m.clipboardAction))

				// Preparar lista de destinos para el modal
				items := []list.Item{
					fileItem{name: "Directorio actual", path: "/ruta/actual", isDirectory: true},
					fileItem{name: "Documentos", path: "/home/user/Documentos", isDirectory: true},
					fileItem{name: "Descargas", path: "/home/user/Descargas", isDirectory: true},
					fileItem{name: "Imágenes", path: "/home/user/Imágenes", isDirectory: true},
				}
				m.modalList = list.New(items, list.NewDefaultDelegate(), 20, 10)
				m.modalList.Title = "Seleccione destino"
				m.modalList.SetShowHelp(false)

				// Preparar contenido
				action := "copiar"
				if m.clipboardAction == "mover" {
					action = "mover"
				}
				m.modalContent = fmt.Sprintf("Seleccione dónde %s \"%s\":",
					action, m.clipboard.name)
			}
		}

	case tea.WindowSizeMsg:
		m.width = msg.Width
		m.height = msg.Height

		// Calcular tamaños para paneles y viewport
		panelWidth := (msg.Width - 4) / 3
		panelHeight := msg.Height / 2

		// Actualizar tamaños de paneles
		for i := range m.panels {
			m.panels[i].SetWidth(panelWidth)
			m.panels[i].SetHeight(panelHeight)
		}

		// Actualizar tamaño de viewport
		m.viewport.Width = msg.Width - 4
		m.viewport.Height = msg.Height - panelHeight - 6

		// Actualizar tamaño de lista modal
		m.modalList.SetWidth(msg.Width / 2)
		m.modalList.SetHeight(msg.Height / 3)
	}

	// Actualizar el panel activo
	var cmd tea.Cmd
	m.panels[m.activePanel], cmd = m.panels[m.activePanel].Update(msg)
	cmds = append(cmds, cmd)

	// Actualizar viewport
	m.viewport, cmd = m.viewport.Update(msg)
	cmds = append(cmds, cmd)

	return m, tea.Batch(cmds...)
}

func (m model) View() string {
	if m.width == 0 {
		return "Inicializando..."
	}

	// Renderizar paneles principales
	panelViews := make([]string, len(m.panels))
	for i, panel := range m.panels {
		if i == m.activePanel {
			panelViews[i] = activeStyle.Width(panel.Width()).Render(panel.View())
		} else {
			panelViews[i] = borderStyle.Width(panel.Width()).Render(panel.View())
		}
	}

	// Unir paneles horizontalmente
	mainView := lipgloss.JoinHorizontal(lipgloss.Top, panelViews...)

	// Viewport para mostrar contenido de archivo
	viewportView := borderStyle.Width(m.viewport.Width).Render(
		titleStyle.Render(" Contenido ") + "\n" + m.viewport.View(),
	)

	// Unir todo verticalmente
	fullView := lipgloss.JoinVertical(lipgloss.Left, mainView, viewportView)

	// Añadir ayuda
	help := "\nNavegar: ↑↓←→ | Tab: cambiar panel | c: copiar | m: mover | p: pegar | q: salir"
	fullView = lipgloss.JoinVertical(lipgloss.Left, fullView, help)

	// Si hay un modal activo, superponer en el centro
	if m.showModal {
		// Calcular dimensiones del modal
		modalWidth := m.width / 2
		// modalHeight := m.height / 3

		var modalContent string

		// Contenido específico según el tipo de modal
		if m.modalType == pasteModal {
			// Modal con lista para seleccionar destino
			modalContent = lipgloss.JoinVertical(
				lipgloss.Left,
				m.modalContent,
				"\n",
				m.modalList.View(),
			)
		} else {
			// Modal simple con texto y botones
			modalContent = m.modalContent
		}

		// Añadir botones
		buttonRow := ""
		for i, btn := range m.modalButtons {
			if i == m.modalSelectedBtn {
				buttonRow += selectedButtonStyle.Render(btn)
			} else {
				buttonRow += buttonStyle.Render(btn)
			}
			buttonRow += " "
		}

		// Construir modal completo
		modalView := lipgloss.JoinVertical(
			lipgloss.Center,
			titleStyle.Render(m.modalTitle),
			"\n",
			modalContent,
			"\n",
			buttonRow,
		)

		// Aplicar estilo al modal
		styledModal := modalStyle.Width(modalWidth).Render(modalView)

		// Calcular posición para centrar
		// modalXPos := (m.width - lipgloss.Width(styledModal)) / 2
		// modalYPos := (m.height - lipgloss.Height(styledModal)) / 2

		// Colocar modal en el centro
		modalPlaced := lipgloss.Place(
			m.width,
			m.height,
			lipgloss.Center,
			lipgloss.Center,
			styledModal,
		)

		// Superponer el modal sobre la vista principal
		return modalPlaced
	}

	return fullView
}

func main() {
	p := tea.NewProgram(initialModel(), tea.WithAltScreen())
	if _, err := p.Run(); err != nil {
		fmt.Printf("Error ejecutando la aplicación: %v", err)
	}
}
