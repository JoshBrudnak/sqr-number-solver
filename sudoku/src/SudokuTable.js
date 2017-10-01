import React, { Component } from "react";
import Button from 'material-ui/Button';
import Paper from 'material-ui/Paper';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
const styles = theme => ({});
class SudokuTable extends Component{
  constructor(){
    super()
    this.state ={
      upload: false,
    };
  }
cell=()=>{
    let tableCell=[];
    let table= [];
    let style ="";
  for (let cell = 0; cell < 9; cell++ ){
    if (cell ===2 || cell ===5 ){
       tableCell.push(
       <td style={{
         border: "1px solid white",
         borderRight: "3px solid white",
         color: "white",
         fontWeight: "bold",
         height: "50px",
         width: "50px",
         backgroundColor: "#1976D2"}} 
         key={cell+"cell"}>
         {cell}
         </td>);
    }else
       tableCell.push(
       <td style={{
         color: "white",
         fontWeight: "bold",
         height: "50px",
         width: "50px",
         border: "1px solid white",
         backgroundColor: "#1976D2"}} 
         key={cell+"cell"}>
         {cell}
         </td>);

     }   
     return tableCell;    
  }
  row=()=>{
    let tableRow= [];
  for (let row = 0; row < 9; row++ ){ 
    if (row ===2 || row ===5 ){       
        tableRow.push(
        <tr style={{borderBottom: "3px solid white"}} 
        key={row+"row"}>{this.cell()}</tr>);
    }else{
       tableRow.push(
        <tr 
        key={row+"row"}>{this.cell()}</tr>);
    }
         console.log(tableRow[row].key , this.cell()[row].key) 
    } 
   return tableRow

  }
 
render(){
    return (
    <Paper style={{width: '100%', justifyContent: "flex"}}>
      <div>
        <Toolbar>
          <Typography type="title" style={{color:"#1976D2",fontWeight: "bold",padding:"10px"}}>
            Square Solver
          </Typography>
          </Toolbar>
      <table  style={{borderCollapse: "collapse"}}>
       <tbody>
    {this.row()}
    </tbody>
    </table>
    </div>
      <form 
      method="post" encType="multipart/form-data">
           <input 
         
         type="file" name="file"/>
         <input 
         style={{
      textTransform:"uppercase",
      lineHeight: '1em',
      boxSizing: 'border-box',
      minWidth: 88,
      minHeight: 36,
      padding: '11px',
      color: "black",
      backgroundColor:"transparent",
      border: "none",
      borderRadius: 2,
      }} 
         type="submit" value="Upload"/>
    </form>
 
  
    <Button flatPrimary> Solve </Button>
    <Button> Reset </Button>  
 </Paper>


    );
}
};
export default (SudokuTable);