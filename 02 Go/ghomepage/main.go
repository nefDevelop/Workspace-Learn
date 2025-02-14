package main

import (
	"log"
	"net/http"
	"os/exec"
)

type Container struct {
	ID     string `json:"ID"`
	Image  string `json:"Image"`
	Names  string `json:"Names"`
	Status string `json:"Status"`
}

func getContainers(w http.ResponseWriter, r *http.Request) {
	//Ejecutamos docker ps y retorne json
	cmd := exec.Command("docker", "ps", "--format")
}

func main() {
	HandleFunc("/container", getContainers)
	log.Println("Servidor en http://localhost:4040")
	log.Fatal(http.ListenAndServe(":4040", nil))
}
