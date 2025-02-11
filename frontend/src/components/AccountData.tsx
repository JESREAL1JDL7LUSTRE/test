import { useEffect, useState } from "react";
import { useAuth } from "@clerk/clerk-react";

export default function AccountData() {
  const { getToken, isSignedIn } = useAuth();
  const [accountData, setAccountData] = useState(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Only fetch data if the user is signed in
    if (isSignedIn) {
        const fetchData = async () => {
            try {
              const token = await getToken();
              console.log("Retrieved Token:", token); // Debugging
          
              if (!token) {
                console.error("No token received");
                return;
              }
          
              const response = await fetch("http://127.0.0.1:8000/api/secure/account-data/", {
                method: "GET",
                headers: {
                  "Authorization": `Bearer ${token}`,
                  "Content-Type": "application/json",
                },
              });
          
              if (!response.ok) {
                throw new Error(`Failed to fetch account data: ${response.statusText}`);
              }
          
              const data = await response.json();
              console.log("User account data:", data);
              setAccountData(data);
            } catch (error) {
              console.error("Error fetching account data:", error);
              setError(error instanceof Error ? error.message : String(error));
            }
          };
          


      fetchData();
    }
  }, [isSignedIn, getToken]); // This effect runs when isSignedIn changes

  if (!isSignedIn) {
    return <div>Please sign in to view your account data.</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!accountData) {
    return <div>Loading account data...</div>;
  }

  return (
    <div>
      <h1>Your Account Data</h1>
      <pre>{JSON.stringify(accountData, null, 2)}</pre>
    </div>
  );
}
