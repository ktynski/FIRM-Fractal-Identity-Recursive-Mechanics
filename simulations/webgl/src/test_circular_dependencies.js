/**
 * Circular Dependency Detection Test
 * Analyzes import statements to detect potential circular dependencies
 */

const fs = require('fs');
const path = require('path');

// Find all JavaScript files
function findJSFiles(dir) {
  const files = [];
  const items = fs.readdirSync(dir);
  
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory()) {
      files.push(...findJSFiles(fullPath));
    } else if (item.endsWith('.js')) {
      files.push(fullPath);
    }
  }
  
  return files;
}

// Extract imports from a file
function extractImports(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const imports = [];
  
  // Match ES6 import statements
  const importRegex = /import\s+.*?\s+from\s+['"`]([^'"`]+)['"`]/g;
  let match;
  
  while ((match = importRegex.exec(content)) !== null) {
    let importPath = match[1];
    
    // Resolve relative imports
    if (importPath.startsWith('./') || importPath.startsWith('../')) {
      importPath = path.resolve(path.dirname(filePath), importPath);
      
      // Add .js extension if missing
      if (!importPath.endsWith('.js') && !fs.existsSync(importPath)) {
        importPath += '.js';
      }
    }
    
    imports.push(importPath);
  }
  
  return imports;
}

// Build dependency graph
function buildDependencyGraph() {
  const files = findJSFiles('./src');
  const graph = {};
  
  for (const file of files) {
    const imports = extractImports(file);
    graph[file] = imports.filter(imp => imp.includes('/src/') || imp.includes('src/'));
  }
  
  return graph;
}

// Detect circular dependencies using DFS
function detectCircularDependencies(graph) {
  const visited = new Set();
  const recursionStack = new Set();
  const cycles = [];
  
  function dfs(node, path = []) {
    if (recursionStack.has(node)) {
      // Found a cycle
      const cycleStart = path.indexOf(node);
      cycles.push([...path.slice(cycleStart), node]);
      return true;
    }
    
    if (visited.has(node)) {
      return false;
    }
    
    visited.add(node);
    recursionStack.add(node);
    
    const dependencies = graph[node] || [];
    for (const dep of dependencies) {
      if (graph[dep] && dfs(dep, [...path, node])) {
        return true;
      }
    }
    
    recursionStack.delete(node);
    return false;
  }
  
  for (const node of Object.keys(graph)) {
    if (!visited.has(node)) {
      dfs(node);
    }
  }
  
  return cycles;
}

// Analyze dependency depth
function analyzeDependencyDepth(graph) {
  const depths = {};
  
  function getDepth(node, visited = new Set()) {
    if (visited.has(node)) return 0; // Circular or already computed
    if (depths[node] !== undefined) return depths[node];
    
    visited.add(node);
    const dependencies = graph[node] || [];
    let maxDepth = 0;
    
    for (const dep of dependencies) {
      if (graph[dep]) {
        maxDepth = Math.max(maxDepth, getDepth(dep, visited) + 1);
      }
    }
    
    visited.delete(node);
    depths[node] = maxDepth;
    return maxDepth;
  }
  
  for (const node of Object.keys(graph)) {
    getDepth(node);
  }
  
  return depths;
}

// Run the analysis
console.log('🔍 Analyzing module dependencies...\n');

const graph = buildDependencyGraph();
const cycles = detectCircularDependencies(graph);
const depths = analyzeDependencyDepth(graph);

console.log(`📊 Found ${Object.keys(graph).length} JavaScript files`);

// Report circular dependencies
if (cycles.length > 0) {
  console.log('\n❌ Circular dependencies detected:');
  cycles.forEach((cycle, i) => {
    console.log(`${i + 1}. ${cycle.map(f => path.basename(f)).join(' → ')}`);
  });
} else {
  console.log('\n✅ No circular dependencies detected!');
}

// Report dependency statistics
console.log('\n📈 Dependency Analysis:');
const depthValues = Object.values(depths);
console.log(`- Maximum dependency depth: ${Math.max(...depthValues)}`);
console.log(`- Average dependency depth: ${(depthValues.reduce((a, b) => a + b, 0) / depthValues.length).toFixed(2)}`);

// Show files with highest dependencies
const sortedByDepth = Object.entries(depths)
  .sort(([,a], [,b]) => b - a)
  .slice(0, 5);

console.log('\n📚 Most complex modules (by dependency depth):');
sortedByDepth.forEach(([file, depth], i) => {
  console.log(`${i + 1}. ${path.basename(file)} (depth: ${depth})`);
});

// Show import counts
const importCounts = Object.entries(graph)
  .map(([file, imports]) => [file, imports.length])
  .sort(([,a], [,b]) => b - a)
  .slice(0, 5);

console.log('\n📥 Modules with most imports:');
importCounts.forEach(([file, count], i) => {
  console.log(`${i + 1}. ${path.basename(file)} (${count} imports)`);
});

console.log('\n' + '='.repeat(50));
if (cycles.length === 0) {
  console.log('✅ Dependency analysis passed! Clean modular architecture.');
} else {
  console.log('❌ Circular dependencies found. Review module structure.');
  process.exit(1);
}
