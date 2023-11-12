# This code implies you already have the software needed to query Azure AD and have approved, authorized user access within your company's organization.

# Specify the input file and output file paths
$inputFile = "C:\Path\to\input.txt"
$outputFile = "C:\Path\to\output.txt"

# Read the list of users from the input file
$users = Get-Content $inputFile

# Initialize an empty array to store the results
$results = @()

# Loop through each username
foreach ($user in $users) {
    # Replace [INSERT COMMANDS] with the appropriate filter or query for your Get-AdUser command
    $adUser = Get-AdUser -Filter [INSERT COMMANDS]

    if ($adUser) {
        $result = [PSCustomObject]@{
            GivenName = $adUser.GivenName
            Surname = $adUser.Surname
            Manager = $adUser.Manager
            Username = $user
        }
    } else {
        $result = [PSCustomObject]@{
            GivenName = "User not found"
            Surname = "User not found"
            Manager = "User not found"
            Username = $user
        }
    }

    # Add the result to the array
    $results += $result
}

# Export the results to the output file as a text file
$results | Format-Table | Out-File -FilePath $outputFile
