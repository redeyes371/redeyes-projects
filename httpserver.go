package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    // Handle requests to the root path with the helloHandler function
    http.HandleFunc("/", helloHandler)

    // Start the server and listen for requests on port 8080
    log.Println("Starting server at port 8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}

// A function that writes a greeting message to the response
func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello,from Golang!")
}
