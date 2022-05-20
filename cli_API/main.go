package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main(){
	res, err := http.Get("http://127.0.0.1:5000")
	if err != nil{
		log.Fatal(err)
	}
	body, err := io.ReadAll(res.Body)
	res.Body.Close()
	if err != nil{
		log.Fatal(err)
	}
	fmt.Printf("%s\n", body)

	fmt.Printf("Hacemos una busqueda\n")
	res, err = http.Get("http://127.0.0.1:5000/search/Cualquiera")
	if err != nil{
		log.Fatal(err)
	}
	body, err = io.ReadAll(res.Body)
	res.Body.Close()
	if err != nil{
		log.Fatal(err)
	}
	fmt.Printf("%s\n", body)

	fmt.Printf("Hacemos una insercion, ingrese un resultado: ")
	var resultado string
	fmt.Scanln(&resultado)
	res, err = http.Get("http://127.0.0.1:5000/admin/"+resultado)
	if err != nil{
		log.Fatal(err)
	}
	body, err = io.ReadAll(res.Body)
	res.Body.Close()
	if err != nil{
		log.Fatal(err)
	}
	fmt.Printf("%s\n", body)
}