/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     neighbors: Node[]
 *     constructor(val?: number, neighbors?: Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 */

function cloneGraph(node: Node | null): Node | null {
	const oldToNew = {}
    
    function dfs(n) {
        if (!n) return

        if (n.val in oldToNew) {
            return oldToNew[n.val]
        }
        const copy = new Node(n.val)
        oldToNew[n.val] = copy
        for(let nei of n.neighbors) {
            copy.neighbors.push(dfs(nei))
        }
        
        return copy
    }
    
    return dfs(node)
};