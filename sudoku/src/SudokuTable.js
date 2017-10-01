import React, { Component } from "react";
import Paper from 'material-ui/Paper';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import {stuff, things} from "./object.js";
import {styles} from './stylesheet.js';
import { withStyles } from 'material-ui/styles';
import PropTypes from 'prop-types'; 
class SudokuTable extends Component{
  constructor(){
    super()
    this.state ={
      upload: false,
    };
  }
  row=()=>{
    let tableRow= [];
  for (let row = 0; row < 9; row++ ){ 
    if (row ===2 || row ===5 ){       
        tableRow.push(
        <tr style={{borderBottom: "3px solid white"}} 
        key={row+"row"}>{this.cell(row)}</tr>);
    }else{
       tableRow.push(
        <tr 
        key={row+"row"}>{this.cell(row)}</tr>);
    }
         console.log(stuff.solved[row]) 
    } 
   return tableRow

  }
  
cell=(row)=>{
    const classes = this.props.classes;
    let tableCell=[];
  for (let col = 0; col < 9; col++ ){
   if (col ===2 || col ===5 ){
       tableCell.push(
       <td className={classes.cellsBorder}
        key={col+"cell"}>
          {this.populateTable(row,col)}
         </td>);
    }else
       tableCell.push(
       <td className={classes.cells}
          key={col+"cell"}
         >
         {this.populateTable(row,col)}
         </td>);
     }   
     return tableCell;    
  }

populateTable=(row,col)=>{
  return stuff.solved[row][col]
}
handleSolve=(row,col)=>{
  return stuff.solved[row][col]

} 
handleUpload=(row, col)=>{  
  if (things.unsolved[row][col]===0){
    return ""
  }else
  return( things.unsolved[row][col])
} 
handleReset=(row,col)=>{
return ""
}
 
render(){
    return (
    <Paper style={{width: '100%', display: "flex"}}>
      <div style={{justifyContent: "center", alignContent: "center"}}>
        <Toolbar>
          <Typography type="title" style={{justifyContent: "center",color:"#2196F3",fontWeight: "bold",padding:"10px"}}>
            Square Solver
          </Typography>
          </Toolbar>
      <table   style={{borderCollapse: "collapse",justifyContent: "center"}}>
       <tbody>
    {this.row()}
    </tbody>
    </table>
   <div >
    <form className="mui-form"
      method="post" encType="multipart/form-data" >
    <input id="hidden" style={{visibility:"hidden"}}       
         type="file" name="file"/>
  
  <input style={{visibility:"hidden"}}  
         type="submit" id="upload"/>  
  
    </form>
    
    <button onClick={() => {this.getElementById("hidden").click()}} 
    className="mui-btn mui-btn--primary"> 
    Choose
</button>
<button onClick={() => {this.getElementById("upload").click()}} 
    className="mui-btn mui-btn--primary">Upload </button>
     <button onClick={() => {this.handleSolve()}}
       className="mui-btn mui-btn--primary" > Solve </button>  
     <button onClick={() => {this.handleReset()}}
        className="mui-btn mui-btn--primary" > Reset </button> 
    </div> 
    </div>
 </Paper>


    );
}
};
SudokuTable.propTypes = {
  classes: PropTypes.object.isRequired,
};
export default withStyles(styles)(SudokuTable);