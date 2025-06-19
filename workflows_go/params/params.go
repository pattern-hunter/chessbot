package params

type LichessParams struct {
	Username string
	Since    int64
}

type FileWriteParams struct {
	Contents string
}

type ParseDataParams struct {
	Filename string
}
