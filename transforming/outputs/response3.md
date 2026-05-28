# ===== Version 6 - Format Conversion =====

To convert the provided JSON dictionary into an HTML table, you can use the following HTML code. This code includes a title and column headers for the table.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Restaurant Employees</title>
    <style>
      table {
        width: 50%;
        border-collapse: collapse;
        margin: 20px 0;
      }
      th,
      td {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }
      th {
        background-color: #f2f2f2;
      }
    </style>
  </head>
  <body>
    <h1>Restaurant Employees</h1>

    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Shyam</td>
          <td>shyamjaiswal@gmail.com</td>
        </tr>
        <tr>
          <td>Bob</td>
          <td>bob32@gmail.com</td>
        </tr>
        <tr>
          <td>Jai</td>
          <td>jai87@gmail.com</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
```

### Explanation:

- The `<h1>` tag is used for the title of the page.
- The `<table>` element contains the structure of the table.
- The `<thead>` section defines the headers of the table, which are "Name" and "Email".
- The `<tbody>` section contains the actual data rows for each employee.
- Basic CSS is included to style the table for better readability.
