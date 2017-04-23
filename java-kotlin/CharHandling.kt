object CharHandling {
    fun encodingToUtf8(src: String): String {
        return java.lang.String(src.toByteArray(), "UTF-8") as String
    }
}