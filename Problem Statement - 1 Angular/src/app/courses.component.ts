import {Component} from "@angular/core";
import {CoursesService} from "./courses.service"
import {HttpClient} from "@angular/common/http"

@Component({
    selector:"courses",
    
    templateUrl:'./courses.component.html'

})
export  class CoursesComponent{
    
    title3: JSON;
    
    // courses;
    serverData;
    constructor(service: CoursesService, private httpClient: HttpClient){
        
        // this.courses=service.getCourse();
        this.text();
        
        
    }
    
    text() {
        
        this.httpClient.get('http://127.0.0.1:5000/problem').subscribe(data => {
                 this.title3=data as JSON;
                for(let i=0;i<3;i++){ 
                 this.title.push(this.title3[i]['CourseName'])
                 this.courses.push(this.title3[i]['CourseName']);
                 this.section.push(this.title3[i]['Section']);
                 this.data[i] = []
                 this.data[i] = [["Lecture",this.title3[i]['LectureAverage']]];
                 this.data[i].push(["Non Lecture",this.title3[i]['NonlectureAverage']])
                }
                // console.log(this.data);
        })
        
    }
    
    title=[];
    type = 'BarChart';
    data = [];
        //     data = [
//     [
//         ["2012", 900],
//         ["2013", 1000],
//         ["2014", 1170],
//         ["2015", 1250],
//         ["2016", 1530]
//     ],
//     [
//         ["2012", 900],
//         ["2013", 1000],
//         ["2014", 1170],
//         ["2015", 1250],
//         ["2016", 1530]
//     ],
//     [
//         ["2012", 900],
//         ["2013", 1000],
//         ["2014", 1170],
//         ["2015", 1250],
//         ["2016", 1530]
//     ]

//  ];
    columnNames = ['Execution_Method', 'Average_score'];
    options = { };
    width = 550;
    height = 400;
    section=[];
    courses=[];
    props = {
        
        title: this.title, 
        type:this.type, 
        data: this.data,
        columnNames: this.columnNames,
        width: this.width,
        height:this.height,
        section: this.section,
        courses:this.courses
    }
    
}
 
