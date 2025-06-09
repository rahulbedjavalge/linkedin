import webbrowser
import time
import os
from urllib.parse import quote_plus

class LinkedInNavigator:
    def __init__(self):
        """Initialize LinkedIn Browser Navigator"""
        self.base_url = "https://www.linkedin.com"
        print("🔗 LinkedIn Browser Navigator Initialized")
        print("This tool will open LinkedIn pages in your default browser")
        
    def open_latest_posts(self):
        """Open LinkedIn feed with latest posts (sorted by recent)"""
        # Multiple parameters to force recent posts
        import random
        timestamp = int(time.time())
        random_param = random.randint(1000, 9999)
        
        # Try different URL combinations that work better
        feed_url = f"{self.base_url}/feed/?sortBy=recent&t={timestamp}&r={random_param}"
        print("📱 Opening LinkedIn Feed (Latest/Recent Posts)...")
        print("💡 Tip: Once page loads, look for 'Sort by' dropdown and select 'Recent'")
        webbrowser.open(feed_url)
        
    def open_jobs_page(self, keywords="", location=""):
        """Open LinkedIn Jobs page with optional search parameters"""
        if keywords or location:
            # Build job search URL with parameters
            search_params = []
            if keywords:
                search_params.append(f"keywords={quote_plus(keywords)}")
            if location:
                search_params.append(f"location={quote_plus(location)}")
            
            job_url = f"{self.base_url}/jobs/search/?{'&'.join(search_params)}&sortBy=DD"
            print(f"💼 Opening LinkedIn Jobs (Search: {keywords} in {location})...")
        else:
            job_url = f"{self.base_url}/jobs/"
            print("💼 Opening LinkedIn Jobs (Latest Jobs)...")
            
        webbrowser.open(job_url)
        
    def open_trending_posts(self):
        """Open LinkedIn feed sorted by trending/popular posts"""
        trending_url = f"{self.base_url}/feed/?sortBy=relevance"
        print("🔥 Opening Trending LinkedIn Posts...")
        webbrowser.open(trending_url)
        
    def open_latest_posts_fresh(self):
        """Open LinkedIn feed with fresh reload to show newest posts"""
        import random
        timestamp = int(time.time())
        random_param = random.randint(1000, 9999)
        
        # Multiple approaches to force fresh content
        fresh_url = f"{self.base_url}/feed/?sortBy=recent&refresh=true&_={timestamp}&nocache={random_param}"
        print("🆕 Opening Fresh LinkedIn Feed (Newest Posts)...")
        print("💡 If still showing old posts, try manually refreshing the page (Ctrl+F5)")
        webbrowser.open(fresh_url)
        
    def open_activity_feed(self):
        """Open LinkedIn activity feed which shows chronological posts"""
        activity_url = f"{self.base_url}/feed/following/"
        print("⚡ Opening LinkedIn Following Feed (Chronological Order)...")
        print("💡 This shows posts from people/pages you follow in time order")
        webbrowser.open(activity_url)
        
    def open_latest_with_manual_sort(self):
        """Open LinkedIn and provide manual instructions"""
        base_feed = f"{self.base_url}/feed/"
        print("🔧 Opening LinkedIn Feed for Manual Sort...")
        print("\n" + "="*60)
        print("📋 MANUAL STEPS TO SEE LATEST POSTS:")
        print("="*60)
        print("1. Wait for the page to fully load")
        print("2. Look for 'Sort by' dropdown (usually near top of feed)")
        print("3. Click on it and select 'Recent' instead of 'Top'")
        print("4. If no dropdown, try refreshing the page (Ctrl+F5)")
        print("5. On mobile app: Tap the ⚡ icon to switch to Recent")
        print("="*60)
        webbrowser.open(base_feed)
        
    def open_company_jobs(self, company_name):
        """Open jobs from a specific company"""
        company_jobs_url = f"{self.base_url}/jobs/search/?keywords={quote_plus(company_name)}&sortBy=DD"
        print(f"🏢 Opening jobs from {company_name}...")
        webbrowser.open(company_jobs_url)
        
    def open_network_posts(self):
        """Open posts from your network"""
        network_url = f"{self.base_url}/feed/?doFeedRefresh=true&nis=true"
        print("👥 Opening posts from your network...")
        webbrowser.open(network_url)

def main():
    navigator = LinkedInNavigator()
    
    while True:
        print("\n" + "="*50)
        print("🔗 LINKEDIN BROWSER NAVIGATOR")
        print("="*50)
        print("1. 📱 View Latest Posts (Recent Sort)")
        print("2. 🆕 View Fresh Latest Posts (Force Refresh)")
        print("3. ⚡ View Following Feed (Chronological)")
        print("4. 🔧 Manual Sort Instructions")
        print("5. 💼 View Latest Jobs")
        print("6. 🔍 Search Jobs (with keywords)")
        print("7. 🔥 View Trending Posts")
        print("8. 👥 View Network Posts")
        print("9. 🏢 Search Company Jobs")
        print("10. ❌ Exit")
        print("="*50)
        
        try:
            choice = input("Choose an option (1-10): ").strip()
            
            if choice == '1':
                navigator.open_latest_posts()
                
            elif choice == '2':
                navigator.open_latest_posts_fresh()
                
            elif choice == '3':
                navigator.open_activity_feed()
                
            elif choice == '4':
                navigator.open_latest_with_manual_sort()
                
            elif choice == '5':
                navigator.open_jobs_page()
                
            elif choice == '6':
                keywords = input("Enter job keywords (e.g., 'Python Developer'): ").strip()
                location = input("Enter location (e.g., 'New York' or leave empty): ").strip()
                navigator.open_jobs_page(keywords, location)
                
            elif choice == '7':
                navigator.open_trending_posts()
                
            elif choice == '8':
                navigator.open_network_posts()
                
            elif choice == '9':
                company = input("Enter company name: ").strip()
                if company:
                    navigator.open_company_jobs(company)
                else:
                    print("Please enter a company name")
                    
            elif choice == '10':
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please select 1-10.")
                
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("\n✅ Browser tab opened! Check your browser.")
                if choice in ['1', '2', '3']:
                    print("🔄 If you still see old posts, try these steps:")
                    print("   • Clear LinkedIn cookies/cache in your browser")
                    print("   • Hard refresh the page (Ctrl+F5 or Cmd+Shift+R)")
                    print("   • Look for 'Sort by' dropdown and select 'Recent'")
                input("Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 Starting LinkedIn Browser Navigator...")
    print("Make sure you're logged into LinkedIn in your browser!")
    main()
    