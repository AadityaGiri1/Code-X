import java.io.*;
import java.util.*;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    // Function to create a new user account
    public static void createAccount() {
        System.out.println("Enter a username: ");
        String username = scanner.nextLine();
        System.out.println("Enter a password: ");
        String password = scanner.nextLine();
        Map<String, String> userData = new HashMap<>();
        userData.put("username", username);
        userData.put("password", password);
        try (FileWriter fileWriter = new FileWriter(username + "_data.json")) {
            fileWriter.write(new Gson().toJson(userData));
            System.out.println("Account created successfully.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Function to login
    public static String login() {
        System.out.println("Enter your username: ");
        String username = scanner.nextLine();
        System.out.println("Enter your password: ");
        String password = scanner.nextLine();
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(username + "_data.json"))) {
            String jsonData = bufferedReader.readLine();
            Map<String, String> userData = new Gson().fromJson(jsonData, Map.class);
            if (userData.get("password").equals(password)) {
                System.out.println("Login successful.");
                return username;
            } else {
                System.out.println("Incorrect password.");
                return null;
            }
        } catch (IOException e) {
            System.out.println("User not found.");
            return null;
        }
    }

    // Function to manage inventory
    public static void manageInventory(String username, String password) {
        if (!authenticate(username, password)) {
            System.out.println("Authentication failed.");
            return;
        }

        String filename = username + "_inventory.json";
        Map<String, Map<String, Object>> inventory;
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filename))) {
            inventory = new Gson().fromJson(bufferedReader.readLine(), Map.class);
        } catch (IOException e) {
            inventory = new HashMap<>();
        }

        while (true) {
            System.out.println("\n1. Add product");
            System.out.println("2. Update product stock");
            System.out.println("3. View inventory");
            System.out.println("4. Exit");
            System.out.println("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    // Add product
                    // Similar logic as in Python, adapt accordingly
                    break;
                case "2":
                    // Update product stock
                    // Similar logic as in Python, adapt accordingly
                    break;
                case "3":
                    // View inventory
                    // Similar logic as in Python, adapt accordingly
                    break;
                case "4":
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    // Function to manage staff
    public static void manageStaff(String username, String password) {
        if (!authenticate(username, password)) {
            System.out.println("Authentication failed.");
            return;
        }

        String filename = username + "_staff.json";
        Map<String, Map<String, Object>> staff;
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filename))) {
            staff = new Gson().fromJson(bufferedReader.readLine(), Map.class);
        } catch (IOException e) {
            staff = new HashMap<>();
        }

        while (true) {
            System.out.println("\n1. Add staff");
            System.out.println("2. Update staff details");
            System.out.println("3. View staff");
            System.out.println("4. Exit");
            System.out.println("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {

                case "1":
    System.out.println("Enter product name: ");
    String productName = scanner.nextLine();
    System.out.println("Enter stock quantity: ");
    int stock = Integer.parseInt(scanner.nextLine());
    System.out.println("Enter price: ");
    double price = Double.parseDouble(scanner.nextLine());
    System.out.println("Enter discount percentage: ");
    double discount = Double.parseDouble(scanner.nextLine());
    inventory.put(productName, new HashMap<>());
    inventory.get(productName).put("stock", stock);
    inventory.get(productName).put("price", price);
    inventory.get(productName).put("discount", discount);
    try (FileWriter fileWriter = new FileWriter(filename)) {
        fileWriter.write(new Gson().toJson(inventory));
        System.out.println("Product added successfully.");
    } catch (IOException e) {
        e.printStackTrace();
    }
    break;

                    case "2":
                    System.out.println("Enter staff name: ");
                    String staffName = scanner.nextLine();
                    if (staff.containsKey(staffName)) {
                        System.out.println("Enter new salary: ");
                        double newSalary = Double.parseDouble(scanner.nextLine());
                        System.out.println("Enter new bonus: ");
                        double newBonus = Double.parseDouble(scanner.nextLine());
                        staff.get(staffName).put("salary", newSalary);
                        staff.get(staffName).put("bonus", newBonus);
                        try (FileWriter fileWriter = new FileWriter(filename)) {
                            fileWriter.write(new Gson().toJson(staff));
                            System.out.println("Staff details updated successfully.");
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    } else {
                        System.out.println("Staff not found.");
                    }
                    break;
                
                case "3":
                    // View staff
                    // Similar logic as in Python, adapt accordingly
                    break;
                case "4":
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    // Function for billing
    public static void billing(String username) {
        // Similar logic as in Python, adapt accordingly
    }

    // Function to authenticate user for inventory and staff management
    public static boolean authenticate(String username, String password) {
        String filename = username + "_data.json";
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filename))) {
            String jsonData = bufferedReader.readLine();
            Map<String, String> userData = new Gson().fromJson(jsonData, Map.class);
            if (userData.get("password").equals(password)) {
                return true;
            } else {
                return false;
            }
        } catch (IOException e) {
            return false;
        }
    }

    // Main program
    public static void main(String[] args) {
        while (true) {
            System.out.println("\n1. Create Account");
            System.out.println("2. Login");
            System.out.println("3. Exit");
            System.out.println("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    createAccount();
                    break;
                case "2":
                    String username = login();
                    if (username != null) {
                        while (true) {
                            System.out.println("\n1. Manage Inventory");
                            System.out.println("2. Manage Staff");
                            System.out.println("3. Billing");
                            System.out.println("4. Logout");
                            System.out.println("Enter your choice: ");
                            String innerChoice = scanner.nextLine();
                            switch (innerChoice) {
                                case "1":
                                    System.out.println("Enter password for inventory management: ");
                                    String inventoryPassword = scanner.nextLine();
                                    manageInventory(username, inventoryPassword);
                                    break;
                                case "2":
                                    System.out.println("Enter password for staff management: ");
                                    String staffPassword = scanner.nextLine();
                                    manageStaff(username, staffPassword);
                                    break;
                                case "3":
                                    billing(username);
                                    break;
                                case "4":
                                    break;
                                default:
                                    System.out.println("Invalid choice.");
                            }
                            if (innerChoice.equals("4")) {
                                break;
                            }
                        }
                    }
                    break;
                case "3":
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
