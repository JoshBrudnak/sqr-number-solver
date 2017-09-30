import React, { Component } from "react";
import Button from 'material-ui/Button';
import Paper from 'material-ui/Paper';
import PropTypes from "prop-types"
class SudokuTable extends Component{
cell=()=>{
    let tableCell=[];
    let table= [];
    let style ="";
  for (let cell = 0; cell < 9; cell++ ){
       tableCell.push(
       <td style={{
         border: "1px solid gray",
         height: "50px",
         width: "50px",
          backgroundColor: "lightGray"}} 
          key={cell+"cell"}>
          {cell}
          </td>);
     }

    
     return tableCell;    
  }
  row=()=>{
    let tableRow= [];
  for (let row = 0; row < 9; row++ ){        
        tableRow.push(<tr key={row+"row"}>{row}{this.cell()}</tr>);
         console.log(tableRow[row].key , this.cell()[row].key) 
    } 
   return tableRow

  }
  section=(row,colum)=>{
    let section =[]
    let table =[]
    
}
render(){

    return (

    <Paper style={{width: '100%'}}>
      <div>
      <table>
        <thead>
          <tr>
          <td>        
          Sudoku
          </td>
          </tr>
        </thead>
        <tbody>
    {this.row()}
    </tbody>
    </table>
    </div>
    <Button>Upload </Button>
    <Button> Solve </Button>
    <Button> Reset </Button>
    

      </Paper>


    );
}
};
export default (SudokuTable);