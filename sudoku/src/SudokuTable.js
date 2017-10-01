import React, { Component } from "react"
import Paper from "material-ui/Paper"
import Toolbar from "material-ui/Toolbar"
import Typography from "material-ui/Typography"
import { stuff, things, getStuff } from "./object.js"
import { styles } from "./stylesheet.js"
import { withStyles } from "material-ui/styles"
import PropTypes from "prop-types"

class SudokuTable extends Component {
  row = () => {
    return things["unsolved"].map(row => {
      return <tr style={{ alignItems: "center" }}>{this.cell(row)}</tr>
    })
  }

  cell = row => {
    const classes = this.props.classes
    return row.map(item => {
      return <td className={classes.cellsBorder}>{item}</td>
    })
  }

  handleReset = () => {
    let copy = things
    copy["unsolved"].map(item => {
      item = ""
    })
  }

  render() {
    return (
      <Paper style={{ width: "100%", display: "flex" }}>
        <div style={{ justifyContent: "center", alignContent: "center" }}>
          <Toolbar>
            <Typography
              type="title"
              style={{
                justifyContent: "center",
                color: "#2196F3",
                fontWeight: "bold",
                padding: "10px"
              }}
            >
              Square Solver
            </Typography>
          </Toolbar>
          <table
            style={{
              textAlign: "center",
              borderCollapse: "collapse",
              justifyContent: "center"
            }}
          >
            <tbody>{this.row()}</tbody>
          </table>
          <div>
            <button
              onClick={() => {
                document.getElementById("hidden").click()
              }}
              className="mui-btn mui-btn--primary"
            >
              Choose
            </button>
            <button
              onClick={() => {
                document.getElementById("upload").click()
              }}
              className="mui-btn mui-btn--primary"
            >
              UPLOAD
            </button>
            <button
              onClick={() => {
                getStuff().then(grid => {
                  console.log(grid)
                })
              }}
              className="mui-btn mui-btn--primary"
            >
              SOLVE
            </button>
            <button
              className="mui-btn mui-btn--primary"
              onClick={this.handleReset}
            >
              {" "}
              Reset{" "}
            </button>
          </div>
        </div>
      </Paper>
    )
  }
}
SudokuTable.propTypes = {
  classes: PropTypes.object.isRequired
}
export default withStyles(styles)(SudokuTable)
