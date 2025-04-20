function GasStation(strArr) {
    const N = parseInt(strArr[0]); // Total number of gas stations
  
    let totalGas = 0;      // Total gas collected across all stations
    let totalCost = 0;     // Total gas required to complete the full circuit
    let tank = 0;          // Current fuel in tank during simulation
    let startIndex = 0;    // Candidate starting station (0-based)
  
    // Loop through each station
    for (let i = 1; i <= N; i++) {
      const [gas, cost] = strArr[i].split(':').map(Number); // Parse gas and cost at station
  
      totalGas += gas;     // Add to total gas available
      totalCost += cost;   // Add to total cost needed
      tank += gas - cost;  // Simulate fuel gain/loss at current station
  
      // If tank goes negative, current startIndex isn't valid
      if (tank < 0) {
        startIndex = i; // Try the next station as a new starting point
        tank = 0;       // Reset tank since we’re starting fresh
      }
    }
  
    // If total gas is less than total cost, route is impossible
    return totalGas >= totalCost
      ? String(startIndex + 1)  // Return 1-based index if feasible
      : "impossible";           // Otherwise, return "impossible"
  }