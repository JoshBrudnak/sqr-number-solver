import React, { Component } from "react"
import "./App.css"
import SudokuTable from "./SudokuTable.js"
class App extends Component {
  render() {
    return (
      <div className="App">
        <SudokuTable />
      </div>
    )
  }
}

export default App
