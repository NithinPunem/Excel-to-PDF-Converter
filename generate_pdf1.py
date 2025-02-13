from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector

# MySQL connection details
mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'student_data'
}

# Function to fetch data from MySQL
def fetch_data():
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Function to create PDF with 3x2 grid layout for student data
def create_pdf(data):
    c = canvas.Canvas("output1.pdf", pagesize=letter)  # Changed file name to 'output.pdf'
    c.setFont("Helvetica", 9)

    # Define grid layout
    x_start = 30  # Starting X position for grid
    y_start = 750  # Starting Y position for grid
    col_width = 250  # Width of each column (space for 2 columns)
    row_height = 150  # Height of each row (space for 3 rows)

    # Define grid size (3 rows x 2 columns)
    rows_per_page = 3
    cols_per_page = 2

    # Add Title
    c.drawString(x_start, y_start, "Student Data Report")
    y_start -= 30  # Move down after title

    # Keep track of the student count and handle page break after 6 students
    student_count = 0

    # Loop through each student record
    for index, row in enumerate(data):
        if student_count == rows_per_page * cols_per_page:
            c.showPage()  # Create a new page
            c.setFont("Helvetica", 9)
            y_start = 750  # Reset Y position for new page
            c.drawString(x_start, y_start, "Student Data Report")
            y_start -= 30  # Move down after title
            student_count = 0  # Reset student count for the new page

        # Calculate the position of each student's grid cell (3x2 grid)
        row_num = student_count // cols_per_page  # Determine which row
        col_num = student_count % cols_per_page  # Determine which column
        x_pos = x_start + col_num * (col_width + 10)  # Added 10px spacing between columns
        y_pos = y_start - row_num * row_height  # Added more space between rows

        # Display student's details vertically in each cell
        y_offset = y_pos  # Start from top of the cell

        details = [
            f"Course: {row[0]}",
            f"Hallticket No: {row[1]}",
            f"Name: {row[2]}",
            f"Examination: {row[3]}",
            f"Month-Year: {row[4]}",
            f"Branch: {row[5]}",
            f"Subject Code: {row[6]}",
            f"Subject Name: {row[7]}",
            f"DOE: {row[8]}",
            f"Year Code: {row[9]}"
        ]

        # Write each detail vertically in the cell
        for detail in details:
            c.drawString(x_pos, y_offset, detail)
            y_offset -= 12  # Move down to the next line

        student_count += 1  # Increment student count

    # Save the PDF
    c.save()
    print("PDF generated successfully.")

# Fetch data from MySQL and generate PDF
data = fetch_data()
create_pdf(data)
