// This module runs the local gitweb server cgi binary
package main
// https://blog.schroederspace.com/tumbleweed-technology/cgi-a-blast-from-the-past-with-go

import (
	"net/http"
	"net/http/cgi"
	"fmt"
)

//https://pkg.go.dev/net/http/cgi#pkg-types
func cgiHandler(w http.ResponseWriter, r *http.Request) {
	gitweb := cgi.Handler {
		Path: "/usr/share/gitweb/gitweb.cgi",
		Root: "/",
		Dir: "/usr/share/gitweb",
	}
	gitweb.ServeHTTP(w, r)
	fmt.Print("lol")
}

func main() {
	http.HandleFunc("/", cgiHandler)
	http.ListenAndServe(":8080", nil)
}