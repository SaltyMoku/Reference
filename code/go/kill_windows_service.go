package main

import (
	"golang.org/x/sys/windows/svc/mgr"
)

//"golang.org/x/sys/windows/svc/mgr"
//wapi "github.com/iamacarpet/go-win64api"

func main() {
	mgr, err := mgr.Connect()
	if err != nil {
		panic(err.Error())
	}
	srv, err := mgr.OpenService("TeamViewer")
	if err != nil {
		panic(err.Error())
	}
	delete_err := srv.Delete()
	if delete_err != nil {
		panic(err.Error())
	}
}
