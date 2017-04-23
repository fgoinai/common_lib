import org.ini4j.Ini

class IniConf {
    private val ini = Ini(javaClass.classLoader.getResource("conf.ini"))
    private var section = ""

    fun setSection(section: String) : IniConf {
        this.section = section
        return this
    }

    fun getConf(tag: String) : String {
        __isSectionSet()
        return ini.get(section, tag)
    }

    fun getConf(tags: Collection<String>) : HashMap<String, String> {
        __isSectionSet()
        val ret = HashMap<String, String>()
        tags.forEach { ret.put(it, getConf(it)) }
        return ret
    }

    private fun __isSectionSet() {
        if (section == "") throw Exception("Section is not set!")
    }
}