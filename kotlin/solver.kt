import java.io.File
import java.io.InputStream
import java.util.*
import kotlin.collections.ArrayList
import kotlin.system.measureTimeMillis

class Solver {
    var graph = ArrayList< ArrayList<Int> >()
    var numCities = 0
    val NOT_PROCESSED = -1

    var totalHash = 0

    fun init(fileName: String) {
        initGraph(fileName)
    }

    fun initGraph(fileName: String) {
        val inputStream: InputStream = File(fileName).inputStream()
        val lineList = mutableListOf<String>()

        inputStream.bufferedReader().useLines { lines -> lines.forEach { lineList.add(it)} }
        var index = 0
        numCities = lineList[index].toInt()
        index++

        graph = ArrayList< ArrayList<Int> >(numCities)
        for (i in 0..numCities-1) {
            graph.add(ArrayList<Int>())
        }

        // skip mines length
        index++
        // skip mines
        index++

        val numRivers = lineList[index].toInt()
        index++

        for (i in 1..numRivers) {
            val parts = lineList[index].split(' ')
            index++

            val source = parts[0].toInt()
            val target = parts[1].toInt()
            addEdge(source, target)
            addEdge(target, source)
        }
    }

    fun addEdge(source: Int, target: Int) {
        graph[source].add(target)
    }

    fun runBfs(start: Int, result: Array<Int>) {
//        val result = Array<Int>(numCities, {NOT_PROCESSED})
        result[start] = 0

        val queue = ArrayDeque<Int>()
        queue.addLast(start)
        while (queue.isNotEmpty()) {
            val now = queue.pollFirst()
            val value = result[now]

            for (next in graph[now]) {
                if (result[next] == NOT_PROCESSED) {
                    result[next] = value + 1
                    queue.addLast(next)
                }
            }
        }
//        return result
    }

    fun computeHash() {
        val start = java.lang.System.nanoTime()
        // map: city -> mine -> score
        val distances = Array<Array<Int>>(numCities, {
            Array<Int>(numCities, { NOT_PROCESSED })
        })
        for (v in 0..numCities - 1) {
            runBfs(v, distances[v])
        }

        var totalScore = 0
        for (i in 0..numCities - 1) {
            var currentScore = 0
            for (d in distances[i]) {
                if (d == NOT_PROCESSED) {
                    continue
                }
                val d2 = d * d
                currentScore = currentScore xor d2
            }
            totalScore += currentScore
        }
        val end = java.lang.System.nanoTime()
        val timeMs = java.lang.Math.round((end - start) / 1000.0) / 1000.0
        println("time=$timeMs")
        println("graph_hash=$totalScore")
        /* println("name=kotlin") */
    }
}


fun main(args: Array<String>) {
    val s = Solver()

//    val f = "txt-maps/sample.txt"
//    s.init(f)

    s.init(args[1])

    val iters = args[2].toInt()
    for (i in 1..iters) {
        s.computeHash()
        println()
    }
}
