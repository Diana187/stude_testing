function calculateAverage(grades) {
    let sum_of_grades = 0
    for (const i = 0; i < grades.length; i++) {
        sum_of_grades += grades[i]
    }
        
    const average = sum_of_grades/grades.length
    return average;
}

function filterAboveAverageStudents(grades, average) {
    return grades.filter(student => student.grade > average);
}

function main(inputData) {
    // Парсим входные данные
    const lines = inputData.trim().split('\textbackslashn');
    const grades = [];

    for (const line of lines) {
        const [name, gradeStr] = line.split(' ');
        grades.push({ name: name, grade: parseInt(gradeStr) });
    }


    const averageGrade = calculateAverage(grades);

    const aboveAverageStudents = filterAboveAverageStudents(grades, averageGrade);

    const namesAboveAverage = aboveAverageStudents.map(student => student.name).join(' ');
    console.log(namesAboveAverage);
}

// Читаем входные данные
const fs = require('fs');
const input = fs.readFileSync(0, 'utf8');
main(input);